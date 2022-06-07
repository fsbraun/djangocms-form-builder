#####################
 django CMS Frontend
#####################

|pypi| |docs| |coverage| |python| |django| |djangocms|

**djangocms-frontend** supports rendering of styled forms which is part of
all major frontend frameworks, like Bootstrap 5. The objective is to tightly
integrate forms in the website design. Djangocms-frontend allows as many forms
as you wish on one page. All forms are **ajax/xhr-based**. To this end,
djangocms-frontend extends the django CMS plugin model allowing a form plugin
to receive ajax post requests.

There are two different ways to manage forms with **djangocms-frontend**:

1. **Building a form with django CMS' powerful structure board.** This is
   fast an easy. It integrates smoothly with other design elements, especially
   the grid elements allowing to design simple responsive forms.

   Form actions can be configured by form. Built in actions include saving the
   results in the database for later evaluation and mailing submitted forms to
   the site admins. Other form actions can be registered.

   If you prefer to have a central form repository, we suggest
   **djangocms-alias** to manage your forms centrally. Djangocms-alias becomes
   your form editors and forms can be placed on pages by refering to them with
   their alias.

2. **Registering an application-specific form with djangocms-frontend.** If you
   already have forms you may register them with djangocms-frontend and allow
   editors to use them in the form plugin. If you use
   `django-crispy-forms <https://github.com/django-crispy-forms/django-crispy-forms>`_
   all form layouts will be retained. If you only have simpler design
   requirements, **djangocms-frontend** allows you to use fieldsets as with
   admin forms.
**************
 Key features
**************

-  Support of `Bootstrap 5 <https://getbootstrap.com>`_.

-  **Separation of plugins from css framework**, i.e. no need to
   rebuild you site's plugin tree if css framework is changed in the
   future, e.g. from Bootstrap 5 to a future version.


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
<https://github.com/django-cms/djangocms-frontend/graphs/contributors>`_
section.

One of the easiest contributions you can make is helping to translate this addon on
`Transifex <https://www.transifex.com/divio/djangocms-frontend/dashboard/>`_.


Installation
============

For a manual install:

-  run ``pip install djangocms-forms``

-  add ``djangocms_forms`` to your ``INSTALLED_APPS``:

-  run ``python manage.py migrate``

To use the **djangocms-forms** you will have to have
jQuery installed in your project. ``djangocms_frontend`` does not include
jQuery.

Documentation
=============

See readthedocs for the `documentation
<https://djangocms-frontend.readthedocs.io>`_.

.. |pypi| image:: https://badge.fury.io/py/djangocms-frontend.svg
   :target: http://badge.fury.io/py/djangocms-frontend

.. |docs| image:: https://readthedocs.org/projects/djangocms-frontend/badge/?version=latest
    :target: https://djangocms-frontend.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. |coverage| image:: https://codecov.io/gh/fsbraun/djangocms-frontend/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/fsbraun/djangocms-frontend

.. |python| image:: https://img.shields.io/badge/python-3.7+-blue.svg
   :target: https://pypi.org/project/djangocms-frontend/

.. |django| image:: https://img.shields.io/badge/django-3.2-blue.svg
   :target: https://www.djangoproject.com/

.. |djangocms| image:: https://img.shields.io/badge/django%20CMS-3.8%2B-blue.svg
   :target: https://www.django-cms.org/
