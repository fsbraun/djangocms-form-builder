from importlib import import_module

from django.apps import AppConfig
from django.conf import settings
from django.urls import NoReverseMatch, clear_url_caches, include, path, reverse
from django.utils.translation import gettext_lazy as _


class FormsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "djangocms_form_builder"
    verbose_name = _("django CMS form builder")

    def ready(self):
        """Install the URLs"""
        try:
            reverse("form_builder:ajax_form")
        except NoReverseMatch:  # Not installed yet
            urlconf_module = import_module(settings.ROOT_URLCONF)
            urlconf_module.urlpatterns = [
                path(
                    "@form-builder/",
                    include(
                        "djangocms_form_builder.urls",
                        namespace="form_builder",
                    ),
                )
            ] + urlconf_module.urlpatterns
            clear_url_caches()
