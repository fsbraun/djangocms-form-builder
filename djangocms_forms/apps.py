from importlib import import_module

from django.apps import AppConfig
from django.conf import settings
from django.urls import NoReverseMatch, clear_url_caches, include, path, reverse
from django.utils.translation import gettext_lazy as _


class FormsConfig(AppConfig):
    name = "djangocms_forms"
    verbose_name = _("django CMS Forms")

    def ready(self):
        """Install the URLs"""
        try:
            reverse("dcf_forms:ajax_form")
        except NoReverseMatch:  # Not installed yet
            urlconf_module = import_module(settings.ROOT_URLCONF)
            urlconf_module.urlpatterns = [
                path(
                    "@dcf-frontend_forms/",
                    include(
                        "djangocms_forms.urls",
                        namespace="dcf_forms",
                    ),
                )
            ] + urlconf_module.urlpatterns
            clear_url_caches()
