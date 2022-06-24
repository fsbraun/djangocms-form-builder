########################
 django CMS form builder
########################

|pypi| |coverage| |python| |django| |djangocms| |djangocms4|

**djangocms-form-builder** supports rendering of styled forms. The objective is
to tightly integrate forms in the website design. **djangocms-form-builder**
allows as many forms as you wish on one page. All forms are **ajax/xhr-based**.
To this end, **djangocms-form-builder** extends the django CMS plugin model
allowing a form plugin to receive ajax post requests.

There are two different ways to manage forms with **djangocms-form-builder**:

1. **Building a form with django CMS' powerful structure board.** This is
   fast an easy. It integrates smoothly with other design elements, especially
   the grid elements allowing to design simple responsive forms.

   Form actions can be configured by form. Built in actions include saving the
   results in the database for later evaluation and mailing submitted forms to
   the site admins. Other form actions can be registered.

2. Works with **djangocms-alias** to manage your forms centrally. Djangocms-alias becomes
   your form editor and forms can be placed on pages by refering to them with
   their alias.

3. **Registering an application-specific form with djangocms-form-builder.** If you
   already have forms you may register them with djangocms-form-builder and allow
   editors to use them in the form plugin. If you only have simpler design
   requirements, **djangocms-form-builder** allows you to use fieldsets as with
   admin forms.

**************
 Key features
**************

-  Supports `Bootstrap 5 <https://getbootstrap.com>`_.

-  Open architecture to support other css frameworks.

-  Integrates with `django-crispy-forms <https://github.com/django-crispy-forms/django-crispy-forms>`_


Feedback
========

This project is in a early stage. All feedback is welcome! Please
mail me at fsbraun(at)gmx.de

Also, all contributions are welcome.

Contributing
============

This is a an open-source project. We'll be delighted to receive your
feedback in the form of issues and pull requests. Before submitting your
pull request, please review our `contribution guidelines
<http://docs.django-cms.org/en/latest/contributing/index.html>`_.

We're grateful to all contributors who have helped create and maintain
this package. Contributors are listed at the `contributors
<https://github.com/fsbraun/djangocms-form-builder/graphs/contributors>`_
section.



Installation
============

For a manual install:

-  run ``pip install git+https://github.com/fsbraun/djangocms-form-builder@master#egg=djangocms-form-builder``

-  add ``djangocms_form_builder`` to your ``INSTALLED_APPS``:

-  run ``python manage.py migrate``

To use the **djangocms-form-builder** you will have to have
jQuery installed in your project. ``djangocms-form-builder`` does not include
jQuery.


.. |pypi| image:: https://badge.fury.io/py/djangocms-form-builder.svg
   :target: http://badge.fury.io/py/djangocms-form-builder

.. |coverage| image:: https://codecov.io/gh/fsbraun/djangocms-form-builder/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/fsbraun/djangocms-form-builder

.. |python| image:: https://img.shields.io/badge/python-3.7+-blue.svg
   :target: https://pypi.org/project/djangocms-form-builder/

.. |django| image:: https://img.shields.io/badge/django-3.2-blue.svg
   :target: https://www.djangoproject.com/

.. |djangocms| image:: https://img.shields.io/badge/django%20CMS-3.8%2B-blue.svg
   :target: https://www.django-cms.org/

.. |djangocms4| image:: https://img.shields.io/badge/django%20CMS-4%2B-blue.svg
   :target: https://www.django-cms.org/
