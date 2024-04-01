from __future__ import annotations

from collections import deque
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Sequence

    from type_lens import TypeView

    from dtos.plugins import Plugin

__all__ = ("global_plugin_registry",)


class PluginRegistry:
    """A global registry of DTO plugins."""

    __slots__ = ("plugins", "_cache")

    def __init__(self) -> None:
        self.plugins: deque[Plugin] = deque()
        self._cache: dict[TypeView, Plugin] = {}

    def register(self, plugins: Sequence[Plugin]) -> None:
        """Register a DTO plugin.

        Args:
            plugins: Instances of :class:`Plugin` to register.
        """
        self.plugins.extendleft(reversed(plugins))

    def get(self, type_view: TypeView) -> Plugin | None:
        """Get the plugin that can handle the given type.

        Args:
            type_view (TypeView): The type to get the plugin for.

        Returns:
            Plugin | None: The plugin that can handle the given type, or None if not found.
        """
        if plugin := self._cache.get(type_view):
            return plugin

        for plugin in self.plugins:
            if plugin.can_handle(type_view):
                return plugin
        return None

    def copy(self) -> PluginRegistry:
        """Create a new PluginRegistry with the same plugins.

        Returns:
            PluginRegistry: A new PluginRegistry with the same plugins.
        """
        new_registry = PluginRegistry()
        new_registry.plugins = self.plugins.copy()
        return new_registry


global_plugin_registry = PluginRegistry()
