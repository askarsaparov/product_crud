from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.models import CustomUser
from accounts.serializers import ProfileSerializer
from restapp.paginations import ResultsSetPagination


# position list and detail view

@swagger_auto_schema(methods=['get'], responses={200: ProfileSerializer(many=True)}, tags=['user'])
@swagger_auto_schema(
    methods=['post'],
    request_body=ProfileSerializer(),
    responses={200: ProfileSerializer()},
    tags=['user'])
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def listUser(request):
    if request.method == 'POST':
        serializer = ProfileSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    users = CustomUser.objects.all().order_by('id')
    paginator = ResultsSetPagination()
    paginated_users = paginator.paginate_queryset(users, request)
    serializer = ProfileSerializer(paginated_users, many=True, context={'request': request})
    return paginator.get_paginated_response(serializer.data)


@swagger_auto_schema(methods=['get'], responses={200: ProfileSerializer()}, tags=['user'])
@swagger_auto_schema(methods=['delete'], tags=['user'])
@swagger_auto_schema(
    methods=['put'],
    request_body=ProfileSerializer(),
    responses={200: ProfileSerializer()},
    tags=['user'])
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def detailUser(request, id):
    user = get_object_or_404(CustomUser, pk=id)
    if request.method == 'PUT':
        serializer = ProfileSerializer(user, data=request.data, partial=True, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=204)
    serializer = ProfileSerializer(user, context={'request': request})
    return Response(serializer.data, status=200)
