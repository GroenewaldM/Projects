import random

n = input("Level: ")

while n.isdigit() == False or int(n) < 0:
    n = input("Level: ")

output = random.randint(0, int(n))

while True:
    guess = input("Guess: ")
    if guess.isdigit() and int(guess) > 0:
        if int(guess) < output:
            print("Too small!")
        elif int(guess) > output:
            print("Too large!")
        else:
            print("Just right!")
            break
