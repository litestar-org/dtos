from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any

    from type_lens import TypeView

__all__ = (
    "CollectionType",
    "CompositeType",
    "MappingType",
    "NestedFieldInfo",
    "SimpleType",
    "TransferType",
    "TupleType",
    "UnionType",
)


@dataclass(frozen=True)
class NestedFieldInfo:
    """Type for representing fields and model type of nested model type."""

    __slots__ = ("model", "field_definitions")

    model: type[Any]
    types: tuple[TypeView, ...]


@dataclass(frozen=True)
class TransferType:
    """Type for representing model types for data transfer."""

    __slots__ = ("view",)

    view: TypeView


@dataclass(frozen=True)
class SimpleType(TransferType):
    """Represents indivisible, non-composite types."""

    __slots__ = ("nested_field_info",)

    nested_field_info: NestedFieldInfo | None
    """If the type is a 'nested' type, this is the model generated for transfer to/from it."""


@dataclass(frozen=True)
class CompositeType(TransferType):
    """A type that is made up of other types."""

    __slots__ = ("has_nested",)

    has_nested: bool
    """Whether the type represents nested model types within itself."""


@dataclass(frozen=True)
class UnionType(CompositeType):
    """Type for representing union types for data transfer."""

    __slots__ = ("inner_types",)

    inner_types: tuple[CompositeType | SimpleType, ...]


@dataclass(frozen=True)
class CollectionType(CompositeType):
    """Type for representing collection types for data transfer."""

    __slots__ = ("inner_type",)

    inner_type: CompositeType | SimpleType


@dataclass(frozen=True)
class TupleType(CompositeType):
    """Type for representing tuples for data transfer."""

    __slots__ = ("inner_types",)

    inner_types: tuple[CompositeType | SimpleType, ...]


@dataclass(frozen=True)
class MappingType(CompositeType):
    """Type for representing mappings for data transfer."""

    __slots__ = ("key_type", "value_type")

    key_type: CompositeType | SimpleType
    value_type: CompositeType | SimpleType
