# game on guessing a number
#we'll use random library to generate a random number

import random as rm
random_number = rm.randint(0,11)
num = int(input("Guess a number between 0 and 11: "))


while num != random_number:
  num = int(input("Guess a number between 0 and 11: "))
  if(num == random_number):
    print("You guessed it! The number was indeed", random_number)
  else:
    if(num>random_number):
      print("Too high! Try again!")
    else:
      print("Too low! Try again!")
    