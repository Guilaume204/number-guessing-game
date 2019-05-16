import random

hidden = random.randint(1, 100)

print('I am thinking of a number from 1 to 100....can you guess the number???')

guess = int(input("Take a guess: "))

while hidden!="guess":
    if guess == hidden:
        print("Correct!!!")
        break
    if guess > hidden:
        print("Your guess is to high")
        guess = int(input("Take a guess: ")
    if guess < hidden:
       print("Your guess is to low")
       guess = int(input("Take a guess"))
