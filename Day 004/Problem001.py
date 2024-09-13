# Q1. what is a class ?

# 1. variables (attributes)
# 2. methods (function)

# myth  => class consist of variable or methods (this will always not true)
# class is a blue print for creating object.

# concept 1

# 1. variable = small letters
# 2. class = first word must be capital


class Students:
    name = "jai prakash"

    def info(self):
        print("calling from Students class")


obj = Students()
obj.age = 21
print(obj.__dict__)
obj.info()
print(obj.name)


# concept 2 (accessing methods and variables)
# 1. method = ()
# 2. variables = .variableName


# 1. shortcut
# 1. ctrl + shift + z = redo
