# Q what is Docstring . explain with example ?


def greet(name):
    """this is my python program"""
    print(name)
    return name


def add(a, b):
    """this function will add two numbers"""
    return a + b


print(add.__doc__)
print(greet.__doc__)
# print(greet.__annotations__)
