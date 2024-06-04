from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from accounts.views.auth import MyTokenObtainPairView, register, change_password
from accounts.views.enums import get_gender_list
from accounts.views.permission import getPermission
from accounts.views.profile import profile, set_default_image
from accounts.views.role import role, roleId
from accounts.views.user import listUser, detailUser

app_name = 'accounts'

urlpatterns = [

    # Authentication
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', register, name='auth_register'),
    path('change-password/', change_password, name='auth_change_password'),

    # Profile
    path('profile/', profile, name='profile'),
    path('set-default-image/', set_default_image, name='set_default_image'),

    # Role
    path('role/', role, name='role'),
    path('role/<int:id>/', roleId, name='role-id'),

    # Permission
    path('permission/', getPermission, name='permission'),

    # Enums
    path('enum/gender/', get_gender_list, name='enum-gender'),

    # User
    path('user/', listUser, name='list-user'),
    path('user/<int:id>/', detailUser, name='detail-user'),

]
