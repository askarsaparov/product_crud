from datetime import datetime

from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from accounts.models import CustomUser
from accounts.schemas import register_schema, update_password_schema
from accounts.serializers import MyTokenObtainPairSerializer, RegisterSerializer, ChangePasswordSerializer


# Login User
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# Register User
@swagger_auto_schema(methods=['post'],
                     request_body=RegisterSerializer,
                     responses=register_schema,
                     tags=['auth'])
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    # Manually set last_login to the current time
    user = CustomUser.objects.get(email=request.data['email'])
    user.last_login = datetime.now()
    user.save()

    # Log the user in by generating tokens
    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)
    refresh_token = str(refresh)

    # Include both tokens in the response
    response_data = {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "Bearer",
        "user": serializer.data,
    }
    return Response(response_data, status=status.HTTP_201_CREATED)


# Update Password
@swagger_auto_schema(methods=['post'],
                     request_body=ChangePasswordSerializer,
                     responses=update_password_schema,
                     tags=['auth'])
@api_view(['POST'])
def change_password(request):
    serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        # Update the user's password
        user = request.user
        new_password = serializer.validated_data['new_password']
        user.set_password(new_password)
        user.save()

        return Response({'detail': 'Password updated successfully.'}, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
