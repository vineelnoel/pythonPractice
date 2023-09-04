class Practice:
    """
    Decorator example
    """
    @staticmethod
    def convert_upper(func):
        def wrapper(self):
            func_output = func(self)
            print("In convert upper")
            return func_output.upper()

        return wrapper

    @staticmethod
    def split_string(func):
        def wrapper(self):
            func_output = func(self)
            print("In split string")
            return func_output.split()

        return wrapper

    @split_string
    @convert_upper
    def some_func(self):
        return "Hello World!"

    """
    Decorators with params
    """

    @staticmethod
    def convert_upper_with_params(func):
        def wrapper(self, param1, param2):
            param1 = param1.upper()
            param2 = param2.upper()
            func_output = func(self, param1, param2)
            return func_output

        return wrapper

    @convert_upper_with_params
    def say_hello(self, name1, name2):
        return "Hello: " + name1 + " Hello: " + name2

    """
    Fibonacci series
    """

    def fibonacci_series(self, end_number: int) -> None:
        a = 0
        b = 1
        print(f"{a} {b}", end=" ")
        for i in range(end_number):
            c = b
            b = a + b
            a = c
            print(f"{b}", end=" ")


if __name__ == '__main__':
    practice_obj = Practice()
    # print(practice_obj.some_func())
    # print(practice_obj.say_hello("Vineel","Noel"))
    practice_obj.fibonacci_series(8)
