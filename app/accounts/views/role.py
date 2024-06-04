from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.models import Role
from accounts.serializers import RoleSerializer


# api/role
@swagger_auto_schema(methods=['get', 'post'], responses={200: RoleSerializer}, tags=['role'])
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def role(request):
    roles = Role.objects.all()
    if request.method == 'POST':
        serializer = RoleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    serializer = RoleSerializer(roles, many=True)
    return Response(serializer.data)


@swagger_auto_schema(methods=['get', 'put', 'delete'], responses={200: RoleSerializer}, tags=['role'])
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def roleId(request, id):
    role = get_object_or_404(Role, id=id)
    if request.method == 'DELETE':
        role.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'PUT':
        serializer = RoleSerializer(role, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    serializer = RoleSerializer(role)
    return Response(serializer.data)
