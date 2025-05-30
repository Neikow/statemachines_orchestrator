import sys
from functools import lru_cache
from typing import Any


def _get_machines_annotations(
    cls: type,
    cls_annotations: dict[str, Any],
) -> dict[str, type]:
    return {
        machine_name: _get_class(cls, machine_name, cls_annotations[machine_name])
        for machine_name in cls_annotations
    }


@lru_cache
def _get_types(cls: type) -> dict[str, type]:
    typing = sys.modules.get("typing")
    if typing is None:
        raise ModuleNotFoundError("The 'typing' module is not available in sys.modules.")
    return typing.get_type_hints(cls)


def _get_class(cls: type, machine_name: str, type_or_type_name: str | type) -> type:
    if isinstance(type_or_type_name, type):
        return type_or_type_name
    else:
        return _get_types(cls)[machine_name]
