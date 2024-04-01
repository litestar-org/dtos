from __future__ import annotations

from typing import TYPE_CHECKING

import msgspec

from dtos.exc import ConfigError

if TYPE_CHECKING:
    from collections.abc import Set

    from dtos.types import RenameStrategy

__all__ = ("DTOConfig",)


class DTOConfig(msgspec.Struct, frozen=True):
    """Control the generated DTO."""

    exclude: Set[str] = msgspec.field(default_factory=set)
    """Explicitly exclude fields from the generated DTO.

    If exclude is specified, all fields not specified in exclude will be included by default.

    Notes:
        - The field names are dot-separated paths to nested fields, e.g. ``"address.street"`` will
            exclude the ``"street"`` field from a nested ``"address"`` model.
        - 'exclude' mutually exclusive with 'include' - specifying both values will raise an
            ``ImproperlyConfiguredException``.
    """
    include: Set[str] = msgspec.field(default_factory=set)
    """Explicitly include fields in the generated DTO.

    If include is specified, all fields not specified in include will be excluded by default.

    Notes:
        - The field names are dot-separated paths to nested fields, e.g. ``"address.street"`` will
            include the ``"street"`` field from a nested ``"address"`` model.
        - 'include' mutually exclusive with 'exclude' - specifying both values will raise an
            ``ImproperlyConfiguredException``.
    """
    rename_fields: dict[str, str] = msgspec.field(default_factory=dict)
    """Mapping of field names, to new name."""
    rename_strategy: RenameStrategy | None = None
    """Rename all fields using a pre-defined strategy or a custom strategy.

    The pre-defined strategies are: `upper`, `lower`, `camel`, `pascal`.

    A custom strategy is any callable that accepts a string as an argument and
    return a string.

    Fields defined in ``rename_fields`` are ignored."""
    max_nested_depth: int = 1
    """The maximum depth of nested items allowed for data transfer."""
    partial: bool = False
    """Allow transfer of partial data."""
    underscore_fields_private: bool = True
    """Fields starting with an underscore are considered private and excluded from data transfer."""

    def __post_init__(self) -> None:
        if self.include and self.exclude:
            msg = "Cannot specify both 'include' and 'exclude' in DTOConfig"
            raise ConfigError(msg)
