## Esy mod

def decorator(func):
    def wrapper():
        print("Start")
        func()
        print('End')
    return wrapper


@decorator
def foo():
    ...

foo()

########## timer

import time
from functools import wraps
import inspect

def timer(func):
    @wraps(func)
    def wrapper():
        start_time = time.perf_counter()
        result = func()
        end_time = time.perf_counter()
        duration_sec = end_time - start_time
        print(duration_sec)
        return result
    return wrapper

@timer
def slowpoke():
    """Медленная функция с докстрингом"""
    a = 0
    time.sleep(a)
    return f"Вот это я поспал {a} сек!"

print(slowpoke())

print(f"{'-' * 20}")

################# Трена 2 17.03.25
# Работа с аргументами декорируемой функции в декораторе
from functools import wraps
import gc

# аргументы декорируемой функции в декораторе
def func_announcer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"{' ' * 4}Вызов функции {func.__name__} c args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{' ' * 4}Результат: {result}")
        return result
    return wrapper

# таймер + аргументы
def timer_with_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        duration_sec = end_time - start_time
        print(f"{' ' * 4}Выполнения функции {func.__name__} с args={args}, kwargs={kwargs} заняло {duration_sec}")
        return result
    return wrapper

# Замыкание - счётчик
def counter_decorator(func):
    count = 0
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Вызов #{count}")
        result = func(*args, **kwargs)
        return result
    return wrapper

# Замыкание - лог + извлечение/отображение аргументов как в при вызове
def logger_with_signatures(func):
    log = []

    @wraps(func)
    def wrapper(*args, **kwargs):
        sig = inspect.signature(func)
        bound = sig.bind(*args, **kwargs) # <BoundArguments (text='bilbo is bad')>
        bound.apply_defaults() # <BoundArguments (text='bilbo is bad', default_arg=False)>

        params = [f"{name}={repr(value)}" for name, value in bound.arguments.items()]
        called_func = f"{func.__name__}({', '.join(params)})"

        log.append(called_func)
        print(f"Лог вызова функций: {log}")
        result = func(*args, **kwargs)
        return result
    return wrapper

################# Трена 3 19.03.25

# Замыкание - логгер на последние max_log_size записей
def logger_with_limit(max_log_size: int):
    limit = max_log_size
    log = []

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(result)
            log.append(result)
            if len(log) > limit:
                log.pop(0)
            print(f"{' ' * 4}Логгер с лимитом = {limit}: {log}")
            return result
        return wrapper
    return decorator


# Замыкание - Простой кэш
def simple_cache(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        # чекнуть кеш
        sig = inspect.signature(func)
        bound = sig.bind(*args, **kwargs)
        bound.apply_defaults()
        key = tuple(bound.arguments.items())  # Уникальный ключ

        # вернуть готовое решение если есть
        if key in cache:
            print("Есть в cache!")
            return cache[key]

        # если нет - рассчитать решение
        print("Нет в cache! Рассчитываем...")
        result = func(*args, **kwargs)
        # добавить решение в кэш
        cache[key] = result

        return result
    return wrapper

# Замыкание - Кэш с хеширвоанием ключа (1/2)
import hashlib


def make_key(func, args, kwargs):
    arg_str = f"{func.__name__}:{args}:{kwargs}"
    return hashlib.md5(arg_str.encode()).hexdigest()[:16]

def cache_with_hash(func):
    cache = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = make_key(func, args, kwargs)
        
        if key in cache:
            print(f"Есть в кэше с хэшом!")
            result = cache[key]
        else:
            result = func(*args, **kwargs)
            cache[key] = result
        
        print(f"Кэш с хэшированием: {cache}")
        return result
    return wrapper

# Замыкание - Кэш с хэшированием, TTL и sizelimit (2/2)

def cache_with_hash_ttl_lenlimit(ttl: int = 300, len_limit = 1000):
    def decorator(func):
        print("##############")
        cache = {}
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("@@@@@@@@@@@@@@")
            key = make_key(func, args, kwargs)
            
            if key in cache:
                result, timestamp = cache[key]
                if time.time() - timestamp < ttl:
                    print(f"Есть в кэше с хэшем!")
                    return result
                else:
                    print(f'Есть в кэше с хэшем, но просрочен.')
                    del cache[key]
            
            result = func(*args, **kwargs)
            current_time = int(time.time())
            cache[key] = (result, current_time)

            # Ограничение размера
            if len(cache) > len_limit:
                oldest_key = min(cache, key=lambda x: cache[x][1])
                del cache[oldest_key]
            print(f"Кэш с хэшированием: {cache}")
            return result
        return wrapper
    return decorator



@logger_with_limit(2)
@counter_decorator
@logger_with_signatures
@func_announcer
@timer_with_args
@cache_with_hash
@simple_cache
@cache_with_hash_ttl_lenlimit
def uppercase(text: str, default_arg = False):
    """Возвращает переданное имя заглавными символами.
    default = False - тут для демонстрации работы bound.apply_defaults()"""
    return text.upper()

uppercase('bilbo is good')
uppercase('bilbo is bad')
uppercase('bilbo is ugly')

uppercase('bilbo is good')
uppercase('bilbo is bad')
uppercase('bilbo is ugly')

print(time.time())

