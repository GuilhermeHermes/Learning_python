import random

def play():
        play_again = 1
        while play_again == 1:
            while True:
                try:
                    user = input("rock(R), paper(P), Scissor(S): ").lower()
                    if user not in ['r', 'p', 's']:
                        raise ValueError("Invalid input. Please enter 'r', 'p', or 's'.")
                    break
                except ValueError as error:
                    print(error)
            computer = random.choice(['r', 'p', 's'])
            if(user==computer):
                print(f"the computer select {computer}, tie!")
            elif((user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or (user == 's' and computer == 'p')):
                print(f" the computer select {computer}, You won!")
            else:
                print(f"the computer select {computer}, you lost!")
            while True:
                try:
                    play_again = int(input("Do you wanna play again?(1)YES (2)NOT: "))
                    if play_again not in (1,2):
                         raise ValueError("Invalid input. Please enter (1)YES (2)NOT: ")
                    break
                except ValueError as error:
                    print(error)
play()
