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
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)

@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]
