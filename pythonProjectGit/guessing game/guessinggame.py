import random

secert_word = ["cat", "dog", "wolf", "fox"]
answer = random.choice(secert_word)


guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
print(F"you have {guess_limit} attempts")

def guess_prompt():
    global guess
    global guess_count
    guess = input("Enter a guess: ")
    guess_count += 1

while guess != answer and not (out_of_guesses):
    if guess_count < guess_limit:
        guess_prompt()
    else:
        out_of_guesses = True


if out_of_guesses:
    print("you loose.")
    print(f"the answer was {answer}")
else:
    print("you win!")
