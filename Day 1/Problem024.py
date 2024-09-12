# Q finding factorial of a number


number = int(input("Enter the number you want to find factorial: "))
# def factorial(num):
#     if num < 0:
#         raise ValueError("Factorial is not defined for negative numbers")
#     elif num == 0:
#         return 1
#     else:
#         return num * factorial(num - 1)
# print(factorial(number))

#method 2
fact = 1
if(number==0):
    print(f"{number} factorial is 1")
elif(number<0):
    print(f"{number} factorial is not defined_)))")
else:
    for i in range(1,number+1):
      fact*=i
print(fact)

