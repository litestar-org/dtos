from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from type_lens import TypeView
    from type_lens.parameter_view import ParameterView

__all__ = (
    "DataclassPlugin",
    "MsgspecPlugin",
    "Plugin",
)


class Plugin(ABC):
    @abstractmethod
    def parse_annotation(self, type_view: TypeView) -> tuple[ParameterView, ...]: ...

    @abstractmethod
    def can_handle(self, type_view: TypeView) -> bool: ...


class DataclassPlugin(Plugin):
    def parse_annotation(self, type_view: TypeView) -> tuple[ParameterView, ...]:
        return ()

    def can_handle(self, type_view: TypeView) -> bool:
        return False


class MsgspecPlugin(Plugin):
    def parse_annotation(self, type_view: TypeView) -> tuple[ParameterView, ...]:
        return ()

    def can_handle(self, type_view: TypeView) -> bool:
        return False
