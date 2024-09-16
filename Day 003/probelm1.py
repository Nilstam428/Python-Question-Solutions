# 1. name = "yourName"
# 2. function => "python"
# 3. function => odd / even
# 4. function => table print
# Table printing


name="Nilesh Tamboli"

def get_table(num):
  num = int(input("Enter a number"))
  for i in range(1,11):
    print(f"{num}x{i}={num*i}")

# Even odd
def even_odd(n):
  n = int(input("Enter a number"))
  if(n%2==0):
        print(f"{n} is even !!")
  else:
        print(f"{n} odd number!!")
print(even_odd(n))
