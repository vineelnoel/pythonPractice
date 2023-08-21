"""
Decorator example
"""


def convert_upper(func):
    def wrapper():
        func_output = func()
        return func_output.upper()

    return wrapper


def split_string(func):
    def wrapper():
        func_output = func()
        return func_output.split()

    return wrapper


@split_string
@convert_upper
def some_func():
    return "Hello World!"


print(some_func())


"""
Decorators with params
"""


def convert_upper_with_params(func):
    def wrapper(param1, param2):
        param1 = param1.upper()
        param2 = param2.upper()
        func_output = func(param1, param2)
        return func_output
    return wrapper


@convert_upper_with_params
def say_hello(name1, name2):
    return "Hello: "+name1+" Hello: "+name2


print(say_hello("vineel", "noel"))
