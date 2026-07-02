"""
Задание 4: Декоратор с аргументами (Продвинутое)

Напиши декоратор @retry(retries=3, delay=1), который пытается выполнить функцию 
заданное количество раз (retries), если она выбрасывает исключение. Между 
попытками должна быть пауза в delay секунд. Если все попытки исчерпаны, 
исключение должно пробрасываться дальше.

Подсказка: используй блок try...except внутри цикла и time.sleep() для паузы.

"""
import time
from functools import wraps


# decorator
def retry(retries: int = 3, delay:int = 1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(retries):
                try: 
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Попытка {attempt+1}/{retries}")
                    print(f"Ошибка: {e.__class__.__name__}")

                    if attempt == retries - 1:
                        raise e

                    time.sleep(delay)
        return wrapper
    return decorator


# function
@retry(4, 1)
def exception_raiser():
    try:
        a = 99 / 0
    except ZeroDivisionError:
        print(f"Ошибка: {ZeroDivisionError}")
        raise ZeroDivisionError
