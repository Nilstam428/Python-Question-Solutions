# Q write a function to check (number is prime or not)


# concept 1
# eg : 2, 3, 5, 7, 11, 13,


def checkPrime(number):
    if number < 2:
        print("number is not a prime number")
    elif number == 2:
        print("2 is a prime number")
    elif number > 2:
        for i in range(2, number):
            if number % i == 0:
                print(f"{number} is not a prime number because it is divided by {i}")
                break
        else:
            print(f"{number} is a prime number")
    else:
        print("invalid input")


checkPrime(13)


# while True:
#     for i in range(1, 10):
#         if i == 8:
#             print("out of loop")
#     break
