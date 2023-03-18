import random

def play():
        play_again = 1
        while play_again == 1:
            user = input("rock(R), paper(P), Scissor(S): ".lower())
            computer = random.choice(['r', 'p', 's'])
            if(user==computer):
                print(f"the computer select {computer}, tie!")
            elif((user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or (user == 's' and computer == 'p')):
                print(f" the computer select {computer}, You won!")
            else:
                print(f"the computer select {computer}, you lost!")

            play_again = int(input("Do you wanna play again?(1)YES (2)NOT: "))
play()
