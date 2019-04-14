from functools import wraps


def func_time_decorator(func):
    from datetime import datetime as DATE
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = DATE.now()
        func(*args, **kwargs)
        end_time = DATE.now() - start_time
        print(f'Decorated function work time: {end_time}')
    return wrapper


def call_count_decorator(func):
    counter = 0
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal counter
        func(*args, **kwargs)
        counter += 1
        print(
            f'Decorated function "{func.__name__}" was called {counter} times')
    return wrapper


def show_func_name_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print(
            f'The name of decorated func is {func.__name__}.\n Arguments: positional - {args}, named - {kwargs}')
    return wrapper
