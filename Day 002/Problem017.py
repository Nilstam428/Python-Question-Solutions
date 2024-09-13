# Q what is high order function. Explain with example ?


def double(value):
    return value * 2


def add(double, a, b):
    result = a + b
    print(double(result))
    print(result)


add(double, 5, 10)
