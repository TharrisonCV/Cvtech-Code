import random

userlimit = int(input("Limit the number to: "))

answer = random.randint(1, userlimit)

while True:
    userguess = int(input("Guess a number: "))


    if userguess == answer:

        print("correct!")
        print("this is the answer: " + str(answer))
        break

    else:
        print("Wrong guess, Try again.")