"""
Задание 3: Написание декоратора

Напиши декоратор @timeit, который измеряет время выполнения функции и выводит 
его на экран.
Подсказка: используй модуль time и функцию time.time().
Не забудь про functools.wraps!

Примени этот декоратор к функции, которая выполняет какую-то долгую операцию 
(например, цикл на миллион итераций).
"""

import time
from functools import wraps


def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        print(f"Запуск {func.__name__}")
        result = func(*args, **kwargs)
        print(result)
        duration = time.perf_counter() - start_time
        print(f"Время выполнения {func.__name__}: {duration:.4f}")
        return result
    return wrapper

@timeit
def slow_func(sec) -> str:
    time.sleep(sec)
    return f"Ох как я сладко спал, себе со смехом он сказал"

slow_func(1)
