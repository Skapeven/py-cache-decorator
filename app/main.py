from typing import Callable


def cache(func: Callable) -> Callable:
    vault = {}
    def wrapper(*args, **kwargs):
        if (args) in vault:
            print("Getting from cache")
        else:
            print("Calcultating new result")
            vault[args] = func(*args)
    return wrapper

@cache
def subtraction(a, b):
    return a - b

@cache
def addition(a, b):
    return a + b

@cache

subtraction(1, 1)
addition(1, 1)
subtraction(1, 1)
addition(1, 1)
