# def deco():
#     ...

# def my_func():
#     return 124

# # my_func = my_func(deco)

#############

# from typing import Callable
# import time

# # decorator, func with arguments
# def time_counter(func: Callable):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         res = func(*args, **kwargs)
#         end = time.time()
#         print(f'Время выполнения функции: {end - start}')
#         return res
#     return wrapper


# @time_counter
# def wait_two_sec():
#     time.sleep(2)
#     return 'Функция выполнена'

# #print(wait_two_sec())

# # param

# @time_counter
# def wait_some_sec(sleep_time: int):
#     time.sleep(sleep_time)
#     return 'Функция выполнена'

# print(wait_some_sec(4))


# decorator with param
# def limit_calls(max_calls: int):
#     current_limit = max_calls
#     if not current_limit:
#         raise Exception('Превышен лимит вызовов')
#     def wrapper(func: Callable):
#         def inner(*args, **kwargs):
#             res = my_func(*args, **kwargs)
#             return res
#         return inner
#     return wrapper
#     current_limit -= 1



# @limit_calls(2)
# def my_func(sleep_time: int):
#     time.sleep(sleep_time)
#     return 124

# print(my_func(2))


#############################

import time
from typing import Callable
from functools import wraps



def deco_limit_calls(max_calls: int):
    def wrapper(func: Callable):
        @wraps(func)
        def inner(*args, **kwargs):
            nonlocal max_calls
            if not max_calls:
                raise Exception (f"Достигнуто максимальное количество вызовов {func.__name__}")
            max_calls -= 1
            print(max_calls)
            res = func(*args, **kwargs)
            return res
        return inner
    return wrapper

@deco_limit_calls(2)
def my_func(sleep_time: int):
    """Важный докстринг"""
    time.sleep(sleep_time)
    return "Функиця выполнена!"


print(my_func(1))

print(my_func.__name__)
print(my_func.__doc__)

