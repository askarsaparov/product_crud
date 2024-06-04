from django.shortcuts import get_object_or_404
from django_elasticsearch_dsl.search import Search
from drf_yasg.utils import swagger_auto_schema
from elasticsearch_dsl import Q
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from product.models import Product
from product.schemas import ProductPostSchema, ProductGetSchema, search_param
from product.serializers import ProductSerializer
from restapp.paginations import ResultsSetPagination


# category list and detail view
@swagger_auto_schema(
    methods=['get'],
    responses={200: ProductGetSchema(many=True)},
    tags=['product'],
)
@swagger_auto_schema(
    methods=['post'],
    request_body=ProductPostSchema(),
    responses={200: ProductGetSchema()},
    tags=['product'])
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def listProduct(request):
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    categories = Product.objects.all().order_by('id')
    paginator = ResultsSetPagination()
    paginated_users = paginator.paginate_queryset(categories, request)
    serializer = ProductSerializer(paginated_users, many=True, context={'request': request})
    return paginator.get_paginated_response(serializer.data)


@swagger_auto_schema(methods=['get'], responses={200: ProductGetSchema()}, tags=['product'])
@swagger_auto_schema(methods=['delete'], tags=['product'])
@swagger_auto_schema(
    methods=['put'],
    request_body=ProductPostSchema(),
    responses={200: ProductGetSchema()},
    tags=['product'])
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def detailProduct(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data, partial=True, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=204)
    serializer = ProductSerializer(product, context={'request': request})
    return Response(serializer.data, status=200)


@swagger_auto_schema(
    methods=['get'],
    responses={200: ProductGetSchema(many=True)},
    tags=['product'],
    manual_parameters=search_param
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def searchProduct(request):
    query = request.query_params.get('search')
    if query:
        q = Q(
            'bool',
            should=[
                Q('match', title=query),
                Q('match', description=query),
                Q(
                    'nested',
                    path='category',
                    query=Q('match', category__title=query)
                ),
            ],
            minimum_should_match=1
        )
        search = Search(using='default', index='products').query(q)
        response = search.execute()
        products = [hit.to_dict() for hit in response.hits]
    else:
        products = []
    return Response(products, status=200)
