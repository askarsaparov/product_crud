from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from accounts.manager import UserManager


class Role(Group):
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('role')
        verbose_name_plural = _('roles')


class CustomUser(AbstractUser):
    class Gender(models.TextChoices):
        MALE = 'MALE', 'MALE'
        FEMALE = 'FEMALE', 'FEMALE'

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        null=True,
        blank=True,
        validators=[username_validator]
    )
    middle_name = models.CharField(_("middle name"), max_length=150, blank=True)
    phone = PhoneNumberField(null=True, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    roles = models.ManyToManyField(
        Role,
        verbose_name=_("role"),
        blank=True,
        help_text=_(
            "The roles this user belongs to. A user will get all permissions "
            "granted to each of their roles."
        ),
        related_name="users",
        related_query_name="user_single",
    )
    gender = models.CharField(_('gender'), max_length=10, choices=Gender.choices, blank=True, null=True)
    profile = models.ImageField(_('profile'), upload_to='users/', default='default/profile_picture/image.png', blank=True)
    birthday = models.DateField(_('birthday'), blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def set_default_image(self):
        self.profile = 'default/profile_picture/image.png'
        self.save()

    def __str__(self):
        return f"{self.email}"



