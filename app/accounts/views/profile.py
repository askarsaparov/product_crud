from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.serializers import ProfileSerializer

from drf_yasg.utils import swagger_auto_schema

User = get_user_model()


# api/profile
@swagger_auto_schema(methods=['get'], responses={200: ProfileSerializer}, tags=['auth'])
@swagger_auto_schema(methods=['put'], request_body=ProfileSerializer, responses={200: ProfileSerializer}, tags=['auth'])
@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def profile(request):
    user = request.user
    if request.method == 'PUT':
        serializer = ProfileSerializer(user, data=request.data, partial=True, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    serializer = ProfileSerializer(user, many=False, context={'request': request})
    return Response(serializer.data)

# api/profile
@swagger_auto_schema(methods=['put'], tags=['auth'])
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def set_default_image(request):
    user = request.user
    user.set_default_image()
    user.save()
    return Response({"message": "Set default image successfully updated"})