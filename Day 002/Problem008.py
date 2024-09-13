# Q what is **kwargs ? explain with function's example ?


def function(**kwargs):
    for keys, values in kwargs.items():
        print(f"{keys} : {values}")


function(name="jai", age=21, marks="good")
# dictionary

# for key , values in dict.items():
#     print(f"{key} : {values}")
