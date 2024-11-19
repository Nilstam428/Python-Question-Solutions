# number is divisible by which number

num = int(input("Enter the number"))
divisors = []
for i in range(1, num+1):
  if num % i == 0:
    divisors.append(i)

print(divisors)




