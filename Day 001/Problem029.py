# Q check whether a string include a particuler charcter ?

name = str(input("Enter your desired string: "))
word = str(input("Enter the particular character: "))
found = False
for i in name:
  if i == word:
    found = True
    break
if found:
    print(f"Hooray string contains the character: {word}")
else:
    print(f"Sorry thee string does not contains the character: {word}")