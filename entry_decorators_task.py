# imports for task with decorators
from decorators import func_time_decorator, call_count_decorator, show_func_name_decorator


@call_count_decorator
@show_func_name_decorator
@func_time_decorator
def test_decorated_func(*args, **kwargs):
    print('I\'m a decorated function')


test_decorated_func(1, 2, 3, a=1, b=2)
# Prints:
# I'm a decorated function
# Decorated function work time: 0:00:00.000027
# The name of decorated func is test_decorated_func.
#  Arguments: (1, 2, 3) {'a': 1, 'b': 2}
# Decorated function "test_decorated_func" was called 1 times
