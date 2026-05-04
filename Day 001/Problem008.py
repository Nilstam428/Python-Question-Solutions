# Q how to take list element as a input
# using an for loop or while loop.

# ctrl + b

# element = int(input("Enter number of elements in list :"))
# l1 = []
# for i in range(element):
#     value = int(input("enter value : "))
#     l1.append(value)

# print(l1)


# 1. append = add element (at last position)

# Q. how to take list element as a input using split method (home work)
# using split method
# ele = int(input("Enter the number of elements in the list: "))
# split_list = input("Enter the value with comma seperated: ").split(",")
# print(split_list)

# for numeric list
numeric_list = list(map(int, input("Enter the values separated by space: ").split()))
print(numeric_list)