from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UsernameField

from accounts.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email",)

    def save(self, commit=True):
        user = super().save()
        return user


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = "__all__"
        field_classes = {"email": UsernameField}
