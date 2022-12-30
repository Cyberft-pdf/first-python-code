import random 

def guess(x):
    random_number = random.randint (1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guees a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again. Too low. ")
        elif guess > random_number:
            print("Sorry, guess again. Too hight ")
    
    print(f"Yay, congrats. You have guessed te number {random_number} correctly!!")

guess(10) 

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high (H), too low (L), or correct").lower()
        if feedback == "H":
            high = guess - 1
        elif feedback == "L":
            low = guess + 1
            print("počítač uhodl tvoje číslo")
computer_guess(100)

