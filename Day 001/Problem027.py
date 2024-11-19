# Q find maximum from three numbers. ?

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))

def find_max(a, b, c):
    if a > b:
        max = a
    else:
        max = b
    if c > max:
        return c
    else:
        return max
      
print(find_max(num1, num2, num3))
