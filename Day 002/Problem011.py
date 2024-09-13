# Q find factorial using recursion ?


# concept 1

# recursion = function ke ander function call hoga


def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        return "factorial is not defined"
    else:
        return n * factorial(n - 1)


print(factorial(4))
