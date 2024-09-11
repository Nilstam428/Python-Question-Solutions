# give grade according to marks

# marks = int(input("Enter your marks: "))


# Trying to implement restriction to get true maks only
while True:
    marks = int(input("Enter your marks: "))
    if marks in range(0, 101):
        # Valid input, proceed with further processing
        break
    else:
        print("Invalid input. Please enter a number between 1 and 10.")

if(marks>=90):
  print("Grade: A1")
elif(marks>=80):
  print("Grade: A2")
elif(marks>=70):
  print("Grade: B1")
elif(marks>=60):
  print("Grade: B2")
elif(marks>=50):
  print("Grade: C")
elif(marks>=40):
  print("Grade: D")
elif(marks>=34):
  print("Grade: E")
elif(marks<=33):
  print("Grade: F")
