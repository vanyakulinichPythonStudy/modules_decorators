# imports for task with modules
# import whole module
import testmodule
import re


# all module vars will be in scope of this module
from testmodule import *
print(Basic_Object)  # test print for custom class from module


# copy all testmodule attributes to dict
testmodule_vars = {
    key: getattr(testmodule, key) for key in dir(testmodule) if not re.search('^_{1,}', key)
}

print(testmodule_vars)

# simple class which creates general objects
print(testmodule_vars['Basic_Object'])

# instance
obj = testmodule_vars['Basic_Object']()

obj.set_attr('a', 10)
obj.set_attr('b', 30)
# obj.d = 100  # error, set attributes only be by setter
# print(obj.a) #error, get attributes only by getter
print(obj.get_attr('a'))  # 10
print(obj.get_all_attrs())  # {'a': 10, 'b': 30}
