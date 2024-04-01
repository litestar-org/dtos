from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dtos.config import DTOConfig

__all__ = ("global_config_registry",)


class ConfigRegistry:
    """A global registry of DTO configuration objects."""

    __slots__ = (
        "configs",
        "_cache",
    )

    def __init__(self) -> None:
        self.configs: dict[tuple[type, ...], DTOConfig] = {}
        self._cache: dict[type, DTOConfig] = {}

    def register(self, type_: type, config: DTOConfig) -> None:
        """Register a DTO configuration object.

        Args:
            type_ (type): The type of the DTO object.
            config (DTOConfig): The DTO configuration object.
        """
        self.configs[type_.__mro__] = config

    def get(self, type_: type) -> DTOConfig | None:
        """Get the DTO configuration object for the given type.

        Args:
            type_ (type): The type of the DTO object.

        Returns:
            DTOConfig | None: The DTO configuration object for the given type, or None if not found.
        """
        if config := self._cache.get(type_):
            return config

        for i in range(1, len(type_.__mro__)):
            if config := self.configs.get(type_.__mro__[i:]):
                self._cache[type_] = config
                return config
        return None

    def copy(self) -> ConfigRegistry:
        """Create a new ConfigRegistry with the given configurations added.

        Args:
            configs (dict[type, DTOConfig] | Sequence[tuple[type, DTOConfig]]): The configurations to add.

        Returns:
            ConfigRegistry: A new ConfigRegistry with the given configurations added.
        """
        new_registry = ConfigRegistry()
        new_registry.configs = self.configs.copy()
        return new_registry


global_config_registry = ConfigRegistry()
