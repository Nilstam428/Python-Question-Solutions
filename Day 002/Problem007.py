# What is *args (Non-Keyword Arguments) ? explain with function's example.


def function(*args):
    for i in args:
        print(i)


function("123456", "2", "24")
