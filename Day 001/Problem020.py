# give even number up to n

number = int(input("Enter the number: "))
for i in range(2,number+1,2):
  print(i, end=",")
  
#method 2
for j in range(2,number+1):
  if(j%2==0):   
    print(j, end=",")