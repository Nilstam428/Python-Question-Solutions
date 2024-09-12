# check string is a palindrom or not
#palindrome = same from both the direction
def is_palindrome(s):
  s = ''.join(c for c in s if c.isalnum()).lower() # remove spaces
  return s == s[::-1]
# check string is a palindrome or not
str = str(input("Enter the string you want to check: "))
print(is_palindrome(str)) # True
