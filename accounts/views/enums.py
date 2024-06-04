from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.models import CustomUser
from restapp.utils import enum_serialize


@swagger_auto_schema(methods=['get'], tags=['enum'])
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_gender_list(request):
    return Response(enum_serialize(CustomUser.Gender.choices))
