import random

print ("Number Guessing game")
number = random.randint(1,9)
chance = 0
print ("Guess a nuber between 1 and 9 : ")
while chance < 5: 
    guess = int(input("Enter your Guess : "))
    if guess == number:
        print ("Congratulatins You Won")
        break
    elif guess < number:
        print ("Your guess was too low : Guess a higher Number than ",guess)
    else: 
        print ("Your guess was too high : Guess a Lower Number than ",guess)

    chance += 1
    if not chance < 5:
        print ("YOU LOSE!!! The number is ", number)