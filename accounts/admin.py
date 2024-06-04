from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext_lazy as _

from accounts.forms import CustomUserCreationForm, CustomUserChangeForm
from accounts.models import CustomUser, Role


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("username", "first_name", "last_name", "middle_name", "gender", "profile",
                                          "birthday", "phone",)}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "roles",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    # change_password_form = AdminPasswordChangeForm
    list_display = ("email", "username", "is_staff",)
    list_filter = ("is_staff", "is_superuser", "is_active", "roles", "groups", "gender",)
    search_fields = ("email", "username", "first_name", "last_name", "middle_name",)
    ordering = ("id",)
    filter_horizontal = (
        "roles",
        "groups",
        "user_permissions",
    )


class RoleAdmin(GroupAdmin):
    search_fields = ("name",)
    ordering = ("name",)
    filter_horizontal = ("permissions",)



admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Permission)
admin.site.register(ContentType)
