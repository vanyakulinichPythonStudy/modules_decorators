
import sys
import logging

# test variables
a = 1
b = 'assfasfaf'
c = {'z': 10}
d = [10, 7, 0]
_name = "protected var"


# test function
def get_computer_platform_name():
    return sys.platform


class Decorators():
    @classmethod
    def error_decorator(self, decorated_method):
        def func_wrapper(self, *args, **kwargs):
            try:
                return decorated_method(self, *args, **kwargs)
            except Exception as exception:
                logging.error(
                    f'An error occured in {decorated_method.__name__}\n {exception}')
        return func_wrapper


class Props_Encapsulation():
    def encapsulate_props(self):
        hidden_props = {}

        def props_handler(self, action, name=None, value=None):
            nonlocal hidden_props
            if action == 'get':
                return hidden_props[name]
            if action == 'set':
                hidden_props[name] = value
            if action == 'all':
                return hidden_props
        return props_handler


# simple basic class
class Basic_Object(Props_Encapsulation):

    def __init__(self):
        self.manage_props = super().encapsulate_props()

    # direct setting of attributes is forbidden
    def __setattr__(self, name, value):
        allowed_attrs = ('prop_total_amount', 'manage_props')

        if name in allowed_attrs and not hasattr(self, name):
            object.__setattr__(self, name, value)
        else:
            raise AttributeError(
                'Direct setting of attributes is forbidden. Use setter')

    # attrs setter
    @Decorators.error_decorator
    def set_attr(self, name, value):
        self.manage_props(self, 'set', name, value)

    # attrs getter
    @Decorators.error_decorator
    def get_attr(self, name):
        return self.manage_props(self, 'get', name)

    # get dict with all attrs
    def get_all_attrs(self):
        return self.manage_props(self, 'all')
