class Parent:
    class_var = "I'm a class-level variable in the Parent class"

    @classmethod
    def class_method(cls):
        print("This is a class method in the Parent class")

    @staticmethod
    def static_method():
        print("Static method")


# Accessing class-level variable and method without creating an instance
print(Parent.class_var)
Parent.class_method()
Parent.static_method()
