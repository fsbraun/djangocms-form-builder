from django import forms
from django.apps import apps
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from .helpers import coerce_decimal

if apps.is_installed("captcha"):
    """Soft dependency on django-captcha for reCaptchaField"""

    from captcha.fields import ReCaptchaField  # NOQA
    from captcha.widgets import (  # NOQA
        ReCaptchaV2Checkbox,
        ReCaptchaV2Invisible,
        ReCaptchaV3,
    )

    installed = True

else:
    ReCaptchaV2Invisible = forms.HiddenInput  # NOQA
    ReCaptchaV2Checkbox = forms.HiddenInput  # NOQA
    ReCaptchaV3 = forms.HiddenInput  # NOQA
    installed = False

    class ReCaptchaField:  # NOQA
        def __init__(self, *args, **kwargs):
            pass


WIDGETS = {
    "v2-checkbox": ReCaptchaV2Checkbox,
    "v2-invisible": ReCaptchaV2Invisible,
}


RECAPTCHA_CHOICES = (
    ("v2-checkbox", _("v2 checkbox")),
    ("v2-invisible", _("v2 invisible")),
)


def get_recaptcha_field(config):
    widget_params = {
        "attrs": {
            key: value
            for key, value in config.get("captcha_config", {}).items()
            if key.startswith("data-")
        },
        "api_params": {
            key: value
            for key, value in config.get("captcha_config", {}).items()
            if not key.startswith("data-")
        },
    }
    widget_params["attrs"]["no_field_sep"] = True
    if config.get("captcha_widget", "") == "v3":
        widget_params["attrs"]["required_score"] = coerce_decimal(
            config.get("captcha_requirement", 0.5)
        )
    if not widget_params["api_params"]:
        del widget_params["api_params"]
    field = ReCaptchaField(
        label="",
        widget=WIDGETS[config.get("captcha_widget", "v2-invisible")](
            **widget_params,
        ),
    )
    return field


keys_available = installed and (
    hasattr(settings, "RECAPTCHA_PUBLIC_KEY")
    and hasattr(settings, "RECAPTCHA_PRIVATE_KEY")
)

field_name = "recaptcha_field"
RECAPTCHA_PUBLIC_KEY = getattr(settings, "RECAPTCHA_PUBLIC_KEY", "")
