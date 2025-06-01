import random

def rock_paper_scissors():
    choices = ['rock', 'paper', 'scissors']
    user_score = 0
    comp_score = 0
    while True:
        user = input("Choose rock, paper, or scissors (or 'quit'): ").lower()
        if user == 'quit':
            print(f"Final Score - You: {user_score}, Computer: {comp_score}")
            break
        if user not in choices:
            print("Invalid choice. Try again!")
            continue
        comp = random.choice(choices)
        print(f"You chose {user}, computer chose {comp}.")
        if user == comp:
            print("It's a tie!")
        elif (user == 'rock' and comp == 'scissors') or \
             (user == 'scissors' and comp == 'paper') or \
             (user == 'paper' and comp == 'rock'):
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            comp_score += 1
        print(f"Score - You: {user_score}, Computer: {comp_score}")

rock_paper_scissors()
