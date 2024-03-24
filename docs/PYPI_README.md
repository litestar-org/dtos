# dtos

Model your domain at the edge.

<div align="center">

| Project   |     | Status                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| --------- | :-- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| CI/CD     |     | [![Latest Release](https://github.com/jolt-org/dtos/actions/workflows/publish.yaml/badge.svg)](https://github.com/jolt-org/dtos/actions/workflows/publish.yaml) [![Tests And Linting](https://github.com/jolt-org/dtos/actions/workflows/ci.yaml/badge.svg)](https://github.com/jolt-org/dtos/actions/workflows/ci.yaml) [![Documentation Building](https://github.com/jolt-org/dtos/actions/workflows/docs.yaml/badge.svg)](https://github.com/jolt-org/dtos/actions/workflows/docs.yaml)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Quality   |     | [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=jolt-org_dtos&metric=coverage)](https://sonarcloud.io/summary/new_code?id=jolt-org_dtos) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=jolt-org_dtos&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=jolt-org_dtos) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=jolt-org_dtos&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=jolt-org_dtos) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=jolt-org_dtos&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=jolt-org_dtos) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=jolt-org_dtos&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=jolt-org_dtos)                                                                                                                                                    |
| Community |     | [![Discord](https://img.shields.io/discord/1149784127659319356?labelColor=F50057&color=202020&label=chat%20on%20discord&logo=discord&logoColor=202020)](https://discord.gg/XpFNTjjtTK)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Meta      |     | [![Jolt Project](https://img.shields.io/badge/Jolt%20Org-%E2%AD%90-F50057.svg?logo=python&labelColor=F50057&color=202020&logoColor=202020)](https://github.com/jolt-org/) [![types - Mypy](https://img.shields.io/badge/types-Mypy-F50057.svg?logo=python&labelColor=F50057&color=202020&logoColor=202020)](https://github.com/python/mypy) [![License - MIT](https://img.shields.io/badge/license-MIT-F50057.svg?logo=python&labelColor=F50057&color=202020&logoColor=202020)](https://spdx.org/licenses/) [![Jolt Sponsors](https://img.shields.io/badge/Sponsor-%E2%9D%A4-%23202020.svg?&logo=github&logoColor=202020&labelColor=F50057)](https://github.com/sponsors/jolt-org) [![linting - Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json&labelColor=F50057)](https://github.com/astral-sh/ruff) [![code style - Black](https://img.shields.io/badge/code%20style-black-000000.svg?logo=python&labelColor=F50057&logoColor=202020)](https://github.com/psf/black) |

</div>

> **Warning**: Pre-Release Alpha Stage
>
> Please note that DTOS is currently in a pre-release alpha stage of development. This means the library is still under
> active development, and its API is subject to change. We encourage developers to experiment with DTOS and provide
> feedback, but we recommend against using it in production environments until a stable release is available.`

## About

The `dtos` library bridges the gap between complex domain models and their practical usage across network boundaries.
It is designed for Python developers seeking to streamline the process of configuring different representations of
domain models, such as dataclasses and SQLAlchemy models, for network edge parsing and validation. Whether you're
looking to accept a subset, superset, or a completely customized set of fields defined on your model at the network
edge, `dtos` offers a flexible and powerful solution.

## Purpose

``dtos`` is built with the vision of enhancing domain modeling at the network edge, offering developers unparalleled control
over their data's shape and structure during transfer. The library facilitates:

- **Customizable Data Representations**: Tailor your data to meet the exact needs of your network interactions, enabling
a more efficient and precise data exchange.
- **Edge Parsing and Validation**: Ensure your data integrity by defining explicit parsing and validation rules that
match your application's requirements.
- **Seamless Integration**: Designed to work effortlessly with popular Python data modeling and ORM tools, ``dtos``
integrates into your existing workflow with minimal overhead.

## Contributing

All [Jolt][jolt-org] projects will always be a community-centered, available for contributions of any size.

Before contributing, please review the [contribution guide][contributing].

If you have any questions, reach out to us on [Discord][discord], our org-wide [GitHub discussions][jolt-discussions] page,
or the [project-specific GitHub discussions page][project-discussions].

<hr>

<!-- markdownlint-disable -->
<p align="center">
  <img src="https://raw.githubusercontent.com/jolt-org/branding/473f54621e55cde9acbb6fcab7fc03036173eb3d/assets/Branding%20-%20PNG%20-%20Transparent/Logo%20-%20Banner%20-%20Inline%20-%20Light.png" alt="Litestar Logo - Light" width="100%" height="auto" />
</p>

[jolt-org]: https://github.com/jolt-org
[contributing]: https://docs.dtos.jolt.rs/latest/contribution-guide.html
[discord]: https://discord.gg/XpFNTjjtTK
[jolt-discussions]: https://github.com/orgs/jolt-org/discussions
[project-discussions]: https://github.com/jolt-org/dtos/discussions
[project-docs]: https://docs.dtos.jolt.rs
[install-guide]: https://docs.dtos.jolt.rs/latest/#installation
[newrepo]: https://github.com/organizations/jolt-org/repositories/new?template=dtos
