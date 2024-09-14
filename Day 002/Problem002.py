# Q what is the difference between function's argument and function's parameter
#argument - pass to function parameter

#parameter - variable in function definition

def greet(name):  #parameter
    print(f"Good morning {name}")

greet("Nilesh")   #argument

def hello(name):
    print(name)
    
print(hello(f"Hello this is {"Nilesh"}, my age is {22}"))    