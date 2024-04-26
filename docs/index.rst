=========================
``dtos`` Project Overview
=========================

.. warning:: Pre-Release Alpha Stage

    Please note that ``dtos`` is currently in a pre-release alpha stage of development. This means the library is still
    under active development, and its API is subject to change. We encourage developers to experiment with ``dtos`` and
    provide feedback, but we recommend against using it in production environments until a stable release is available.

    Please see :doc:`releases` for more information on the stability policy.

Introduction
============

The ``dtos`` library bridges the gap between complex domain models and their practical usage across network boundaries.
It is designed for Python developers seeking to streamline the process of configuring different representations of
domain models, such as dataclasses and SQLAlchemy models, for network edge parsing and validation. Whether you're
looking to accept a subset, superset, or a completely customized set of fields defined on your model at the network
edge, ``dtos`` offers a flexible and powerful solution.

Purpose
=======

``dtos`` is built with the vision of enhancing domain modeling at the network edge, offering developers unparalleled control
over their data's shape and structure during transfer. The library facilitates:

- **Customizable Data Representations**: Tailor your data to meet the exact needs of your network interactions, enabling
    a more efficient and precise data exchange.
- **Edge Parsing and Validation**: Ensure your data integrity by defining explicit parsing and validation rules that
    match your application's requirements.
- **Seamless Integration**: Designed to work effortlessly with popular Python data modeling and ORM tools, ``dtos``
    integrates into your existing workflow with minimal overhead.

.. toctree::
    :titlesonly:
    :caption: Documentation
    :hidden:

    usage/index
    reference/index

.. toctree::
    :titlesonly:
    :caption: Development
    :hidden:

    changelog
    contribution-guide
    Available Issues <https://github.com/search?q=user%3Alitestar-org+state%3Aopen+label%3A%22good+first+issue%22+++no%3Aassignee+repo%3A%22dtos%22&type=issues>
    Code of Conduct <https://github.com/litestar-org/.github?tab=coc-ov-file#readme>
