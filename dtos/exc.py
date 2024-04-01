from __future__ import annotations

__all__ = (
    "ConfigError",
    "DtosError",
)


class DtosError(Exception):
    """Base class for exceptions in the ``dtos`` library."""


class ConfigError(DtosError):
    """Raised when there is an error with the configuration of a DTO."""
