import sys
from contextlib import contextmanager


@contextmanager
def missing_module(module_name: str):
    module = sys.modules.pop(module_name, None)
    try:
        yield
    finally:
        if module is not None:
            sys.modules[module_name] = module
