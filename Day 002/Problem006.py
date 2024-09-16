# What is keyword argument and positional argument ? explain with function's example.
# A positional argument is an argument that is passed to a function in the order it is defined in the function’s parameter list
# A keyword argument is an argument that is passed to a function using the parameter name followed by an equals sign (=) and the value. This allows for more flexibility in function calls, as arguments can be passed in any order, and the function can be called with default values or omitted arguments.
# def greet(name):
#     print(f"good morning {name}")


# greet("jd")


# def add(a, b):
#     return a + b


# print(add(5, 10))  # a = 5 , b =10


def add(a, b):
    print(a)
    print(b)
    # return a + b

print(add(b=5, a=10))  # a = 10 , b =5 Positional argument we define the value in function 
 