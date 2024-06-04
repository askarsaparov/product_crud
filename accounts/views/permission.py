from django.contrib.auth.models import Permission
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.serializers import PermissionSerializer


# api/role
@swagger_auto_schema(methods=['get'], responses={200: PermissionSerializer(many=True)}, tags=['role'])
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getPermission(request):
    array = ["outstandingtoken", "blacklistedtoken", "session", "contenttype", "group", "permission", "logentry"]
    permissions = Permission.objects.exclude(content_type__model__in=array)
    serializer = PermissionSerializer(permissions, many=True)
    return Response(serializer.data)
