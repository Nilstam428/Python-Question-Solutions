# Q create a function to add two numbers and store result in 'result' variable.
# create a another function which double value of 'result'


def add(a, b):
    global result
    result = a + b
    return result


print(add(10, 20))


def double(value):
    return value * 2


print(double(result))


# concept 1
# scope of variable
# 1. global variable
# 2. local variable

# name = "radha"  # global variable


# def greet():
#     value = "100"  # local variable


# print(name)
# print(value)


# concept 2
# 1. global
