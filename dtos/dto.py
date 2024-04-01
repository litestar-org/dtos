from __future__ import annotations

from typing import TYPE_CHECKING, Generic, TypeVar

from type_lens.type_view import TypeView

from dtos.internals.config_registry import global_config_registry
from dtos.internals.plugin_registry import global_plugin_registry

if TYPE_CHECKING:
    from collections.abc import Sequence

    from dtos.config import DTOConfig
    from dtos.plugins import Plugin

__all__ = ("DTO",)


T = TypeVar("T")


class DTO(Generic[T]):
    __slots__ = {
        "type_view": "The :class:`TypeView` of the annotation.",
        "_plugin_registry": "Registry for plugins.",
        "_config_registry": "Registry for config objects.",
    }

    def __init__(
        self,
        annotation: type[T],
        *,
        plugins: Sequence[Plugin] = (),
        type_configs: Sequence[tuple[type, DTOConfig]] = (),
    ) -> None:
        self.type_view = TypeView(annotation)

        self._plugin_registry = global_plugin_registry.copy()
        self._plugin_registry.register(plugins)
        self._config_registry = global_config_registry.copy()
        for type_, config in type_configs:
            self._config_registry.register(type_, config)
