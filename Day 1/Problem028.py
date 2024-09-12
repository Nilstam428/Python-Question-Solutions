# find minimum from three numbers

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))

def find_min(a, b, c):
    if a < b:
        min = a
    else:
        min = b
    if c < min:
        return c
    else:
        return min
      
print(find_min(num1, num2, num3))