'''
TASK 4  -   Rock-Paper-Scissors Game
User Input: Prompt the user to choose rock, paper, or scissors.
Computer Selection: Generate a random choice (rock, paper, or scissors) for
the computer.
Game Logic: Determine the winner based on the user's choice and the
computer's choice.
Rock beats scissors, scissors beat paper, and paper beats rock.
Display Result: Show the user's choice and the computer's choice.
Display the result, whether the user wins, loses, or it's a tie.
Score Tracking (Optional): Keep track of the user's and computer's scores for
multiple rounds.
Play Again: Ask the user if they want to play another round.
User Interface: Design a user-friendly interface with clear instructions and
feedback.
'''
import random
list = ['rock','paper','scissors']
user_score = 0
comp_score =0

while True:
    print('''
--------- This is Rock Paper Scissor-game  ----------------
TYPE   ::       Rock - Paper - Scissors    :: only:)         
        ''')
    comp = random.choice(list)
    # Taking input from user 
    print("Enter your choice")
    user=''
    while user not in list:
        user = input().lower()
    

    # logic
    if user ==comp:
        print("\tDRAW")

    # user winning cases --
    elif user == 'paper' and comp =='rock':
        print('\tYOU WIN')
        user_score+=1
    elif user == 'rock' and comp =='scissors':
        print('\tYOU WIN')
        user_score+=1
    elif user == 'scissors' and comp =='paper':
        print('\tYOU WIN')
        user_score+=1

    # computer winning cases ---
    elif user == 'scissors' and comp =='rock':
        print('\tYOU LOSE')
        comp_score+=1
    elif user == 'rock' and comp =='paper':
        print('\tYOU LOSE')
        comp_score+=1
    elif user == 'paper' and comp =='scissors':
        print('\tYOU LOSE')
        comp_score+=1  

    else:
        print("It is not possible hahaha ......") 



    # printing the input of user or computer 
    print(f"\nYour choice was '{user.capitalize()}' and computer's choice was '{comp.capitalize()}'. ")

    # aksing user to play again 
    print("Do you want to play again : ")
    if not input().lower().startswith('y'):
        break

print(f"User total score : {user_score}\nComputer total score : {comp_score}")
print("\n\n ****Thank you for playing this game ****")



