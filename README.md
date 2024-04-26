<!-- markdownlint-disable -->
<p align="center">
  <!-- github-banner-start -->
  <img src="https://raw.githubusercontent.com/litestar-org/branding/main/assets/Branding%20-%20SVG%20-%20Transparent/DTOs%20-%20Banner%20-%20Inline%20-%20Light.svg#gh-light-mode-only" alt="Litestar Logo - Light" width="100%" height="auto" />
  <img src="https://raw.githubusercontent.com/litestar-org/branding/main/assets/Branding%20-%20SVG%20-%20Transparent/DTOs%20-%20Banner%20-%20Inline%20-%20Dark.svg#gh-dark-mode-only" alt="Litestar Logo - Dark" width="100%" height="auto" />
  <!-- github-banner-end -->
</p>
<!-- markdownlint-restore -->

<div align="center">

| Project   |     | Status                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-----------|:----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CI/CD     |     | [![Latest Release](https://github.com/litestar-org/dtos/actions/workflows/publish.yml/badge.svg)](https://github.com/litestar-org/dtos/actions/workflows/publish.yml) [![ci](https://github.com/litestar-org/dtos/actions/workflows/ci.yml/badge.svg)](https://github.com/litestar-org/dtos/actions/workflows/ci.yml) [![Documentation Building](https://github.com/litestar-org/dtos/actions/workflows/docs.yml/badge.svg?branch=main)](https://github.com/litestar-org/dtos/actions/workflows/docs.yml)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Quality   |     | [![Coverage](https://codecov.io/github/litestar-org/dtos/graph/badge.svg?token=vKez4Pycrc)](https://codecov.io/github/litestar-org/dtos) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=litestar-org_dtos&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=litestar-org_dtos) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=litestar-org_dtos&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=litestar-org_dtos) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=litestar-org_dtos&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=litestar-org_dtos) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=litestar-org_dtos&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=litestar-org_dtos)                                                                                                                                                                                                                 |
| Package   |     | [![PyPI - Version](https://img.shields.io/pypi/v/dtos?labelColor=202235&color=edb641&logo=python&logoColor=edb641)](https://badge.fury.io/py/litestar) ![PyPI - Support Python Versions](https://img.shields.io/pypi/pyversions/dtos?labelColor=202235&color=edb641&logo=python&logoColor=edb641) ![DTOs PyPI - Downloads](https://img.shields.io/pypi/dm/dtos?logo=python&label=package%20downloads&labelColor=202235&color=edb641&logoColor=edb641)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Community |     | [![Reddit](https://img.shields.io/reddit/subreddit-subscribers/litestarapi?label=r%2FLitestar&logo=reddit&labelColor=202235&color=edb641&logoColor=edb641)](https://reddit.com/r/litestarapi) [![Discord](https://img.shields.io/discord/919193495116337154?labelColor=202235&color=edb641&label=chat%20on%20discord&logo=discord&logoColor=edb641)](https://discord.gg/litestar) [![Matrix](https://img.shields.io/badge/chat%20on%20Matrix-bridged-202235?labelColor=202235&color=edb641&logo=matrix&logoColor=edb641)](https://matrix.to/#/#litestar:matrix.org) [![Medium](https://img.shields.io/badge/Medium-202235?labelColor=202235&color=edb641&logo=medium&logoColor=edb641)](https://blog.litestar.dev) [![Twitter](https://img.shields.io/twitter/follow/LitestarAPI?labelColor=202235&color=edb641&logo=twitter&logoColor=edb641&style=flat)](https://twitter.com/LitestarAPI) [![Blog](https://img.shields.io/badge/Blog-litestar.dev-202235?logo=blogger&labelColor=202235&color=edb641&logoColor=edb641)](https://blog.litestar.dev)                                                                    |
| Meta      |     | [![Litestar Project](https://img.shields.io/badge/Litestar%20Org-%E2%AD%90%20Advanced%20Alchemy-202235.svg?logo=python&labelColor=202235&color=edb641&logoColor=edb641)](https://github.com/litestar-org/dtos) [![types - Mypy](https://img.shields.io/badge/types-Mypy-202235.svg?logo=python&labelColor=202235&color=edb641&logoColor=edb641)](https://github.com/python/mypy) [![License - MIT](https://img.shields.io/badge/license-MIT-202235.svg?logo=python&labelColor=202235&color=edb641&logoColor=edb641)](https://spdx.org/licenses/) [![Litestar Sponsors](https://img.shields.io/badge/Sponsor-%E2%9D%A4-%23edb641.svg?&logo=github&logoColor=edb641&labelColor=202235)](https://github.com/sponsors/litestar-org) [![linting - Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json&labelColor=202235)](https://github.com/astral-sh/ruff) [![code style - Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/format.json&labelColor=202235)](https://github.com/psf/black) |

</div>

### Model your domain at the edge.

> [!WARNING]
> **Pre-Release Alpha Stage**
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

All [Litestar Organization][litestar-org] projects will always be a community-centered, available for contributions of any size.

Before contributing, please review the [contribution guide][contributing].

If you have any questions, reach out to us on [Discord][discord], our org-wide [GitHub discussions][litestar-discussions] page,
or the [project-specific GitHub discussions page][project-discussions].

<hr>

<!-- markdownlint-disable -->
<p align="center">
  <!-- github-banner-start -->
  <img src="https://raw.githubusercontent.com/litestar-org/branding/main/assets/Branding%20-%20SVG%20-%20Transparent/Organization%20Project%20-%20Banner%20-%20Inline%20-%20Dark.svg" alt="Litestar Logo - Light" width="40%" height="auto" />
  <br>An official <a href="https://github.com/litestar-org">Litestar Organization</a> Project
  <!-- github-banner-end -->
</p>

[litestar-org]: https://github.com/litestar-org
[contributing]: https://docs.dtos.litestar.dev/latest/contribution-guide.html
[discord]: https://discord.gg/litestar
[litestar-discussions]: https://github.com/orgs/litestar-org/discussions
[project-discussions]: https://github.com/litestar-org/dtos/discussions
[project-docs]: https://docs.dtos.litestar.dev
[install-guide]: https://docs.dtos.litestar.dev/latest/#installation
