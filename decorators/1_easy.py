def simple_decorator(func: callable):
    def wrapper():
        print("До функции")
        func()
        print("После")
    return wrapper


def say_hello():
    print("Hello!")

say_hello_deco = simple_decorator(say_hello)