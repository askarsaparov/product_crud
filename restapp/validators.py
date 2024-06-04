from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_isdigit(value):
    if not value.isdigit():
        raise ValidationError(
            _("%(value)s is not a number"),
            params={"value": value},
        )