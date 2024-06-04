from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from product.models import Category
from product.serializers import CategorySerializer
from restapp.paginations import ResultsSetPagination


# category list and detail view
@swagger_auto_schema(methods=['get'], responses={200: CategorySerializer(many=True)}, tags=['category'])
@swagger_auto_schema(
    methods=['post'],
    request_body=CategorySerializer(),
    responses={200: CategorySerializer()},
    tags=['category'])
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def listCategory(request):
    if request.method == 'POST':
        serializer = CategorySerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    categories = Category.objects.all().order_by('id')
    paginator = ResultsSetPagination()
    paginated_users = paginator.paginate_queryset(categories, request)
    serializer = CategorySerializer(paginated_users, many=True, context={'request': request})
    return paginator.get_paginated_response(serializer.data)


@swagger_auto_schema(methods=['get'], responses={200: CategorySerializer()}, tags=['category'])
@swagger_auto_schema(methods=['delete'], tags=['category'])
@swagger_auto_schema(
    methods=['put'],
    request_body=CategorySerializer(),
    responses={200: CategorySerializer()},
    tags=['category'])
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def detailCategory(request, id):
    category = get_object_or_404(Category, pk=id)
    if request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data, partial=True, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=204)
    serializer = CategorySerializer(category, context={'request': request})
    return Response(serializer.data, status=200)
