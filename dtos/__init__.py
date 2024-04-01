from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from dtos.config import DTOConfig
from dtos.dto import DTO
from dtos.internals.config_registry import global_config_registry
from dtos.internals.plugin_registry import global_plugin_registry
from dtos.plugins import DataclassPlugin, MsgspecPlugin

if TYPE_CHECKING:
    from collections.abc import Sequence

    from dtos.plugins import Plugin

__all__ = (
    "DTOConfig",
    "create_dto",
    "register_config",
    "register_plugins",
)

T = TypeVar("T")


def register_config(type_: type, config: DTOConfig) -> None:
    """Register a global DTO configuration object.

    Args:
        type_: The type of the DTO object.
        config: The DTO configuration object.
    """
    global_config_registry.register(type_, config)


def register_plugins(plugins: Sequence[Plugin]) -> None:
    """Register a global DTO plugin.

    Args:
        plugins: Instances of :class:`Plugin` for the :class:`DTO` instance. Additional to any
            plugins already registered. The order of the plugins is important, the first plugin
            that can handle a type is used, and plugins registered later are checked first.
    """
    global_plugin_registry.register(plugins)


def create_dto(
    type_: type[T],
    plugins: Sequence[Plugin] = (),
    type_configs: Sequence[tuple[type, DTOConfig]] = (),
) -> DTO[T]:
    """Create a new DTOFactory with the given configurations added.

    Args:
        type_: The type of the DTO object.
        plugins: Instances of :class:`Plugin` for the :class:`DTO` instance. Additional to, and take
            precedence over plugins registered globally.
        type_configs: A sequence of tuples where the first element is a :class:`type` and the
            second element is a :class:`DTOConfig` instance. Additional to the configurations
            registered globally. Types are matched according MRO, longest match is used.

    Returns:
        A new :class:`DTO` instance.
    """
    return DTO(type_, plugins=plugins, type_configs=type_configs)


register_plugins([DataclassPlugin(), MsgspecPlugin()])
