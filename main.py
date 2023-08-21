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
