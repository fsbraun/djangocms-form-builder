=========
Changelog
=========

0.1.1 (2021-09-14)
==================

* feat: updated captcha optional til active by @svandeneertwegh in https://github.com/fsbraun/djangocms-form-builder/pull/4
* feat: Allow actions to add form fields for configuration by @fsbraun in https://github.com/fsbraun/djangocms-form-builder/pull/6
* fix: Update converage action by @fsbraun in https://github.com/fsbraun/djangocms-form-builder/pull/10
* feat: move to hatch build process by @fsbraun
* ci: Add tests for registry by @fsbraun in https://github.com/fsbraun/djangocms-form-builder/pull/5

New Contributors

* @svandeneertwegh made their first contribution in https://github.com/fsbraun/djangocms-form-builder/pull/4

0.2.0 (unreleased)
=================
* Removed col and rows setting from CharField form plugin
* Set more margin options in spacing between fields
* Fixed anonymous as None to Foregin key 'form_user'
* Added attributesField to every Form plugin for customizing

0.1.0
==================

* Set ``default_auto_field`` to ``BigAutoField`` to ensure projects don't try to create a migration if they still use ``AutoField``
* Transfer of forms app from djangocms-frontend
