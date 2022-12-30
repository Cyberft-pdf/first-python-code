import random 

def guess(x):
    random_number = random.randint (1, x)
    guess = 0
    while guess != random_number:
        gueess != int(input(f"Guees a number between 1 and {x}: "))
        if guess < random_number:
            orint("Sorry, guess again. Too low. ")
        elif guess > random_number:
            print("Sorry, guess again. Too hight ")
    
    print(f"Yay, congrats. You have guessed te number{random_number} correctly!!")

guess(10) 