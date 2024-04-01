from __future__ import annotations

from dtos import DTOConfig, register_config
from dtos.internals.config_registry import global_config_registry


def test_register_global_config_on_object() -> None:
    class Base:
        pass

    class Derived(Base):
        pass

    config = DTOConfig()

    register_config(object, config)

    assert global_config_registry.get(Base) == config
    assert global_config_registry.get(Derived) == config
