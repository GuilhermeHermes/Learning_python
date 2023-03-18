import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    print(f"Guess the number between 1 and {x}")
    while guess != random_number:
            guess = int(input("Guess the number: "))
            if(guess < random_number):
                    print("Guess again! too low... :(")
            elif(guess > random_number):
                    print("Guess again! too high... :(")
    print(f"Congrats! You have gassed the number {guess} correctly")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if(low!=high):
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f"Is guess {guess} too high(H), too low(L) or correctly(C)?:  ".lower())
        if(feedback == 'l'):
                low = guess + 1
        elif(feedback == 'h'):
                high = guess - 1
    print(f"I guess you number {guess} correctly ! :p")

computer_guess(10)



