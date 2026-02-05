from typing import Callable


def cache(func: Callable) -> Callable:
    vault = {}

    def wrapper(*args, **kwargs) -> any:
        if (args) in vault:
            print("Getting from cache")
            return vault[args]
        else:
            print("Calculating new result")
            result = func(*args)
            vault[args] = result
            return result
    return wrapper
