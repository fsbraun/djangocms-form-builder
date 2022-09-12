from django.utils.translation import gettext_lazy as _

from . import settings

default_attr = settings.default_attr  # NOQA
attr_dict = settings.attr_dict  # NOQA
DEFAULT_FIELD_SEP = settings.DEFAULT_FIELD_SEP  # NOQA

CHOICE_FIELDS = (
    (
        _("Single choice"),
        (
            ("select", _("Drop down")),
            ("radio", _("Radio buttons")),
        ),
    ),
    (
        _("Multiple choice"),
        (
            ("checkbox", _("Checkboxes")),
            ("multiselect", _("List")),
        ),
    ),
)
