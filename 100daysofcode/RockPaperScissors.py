import random
rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''


scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''
game_images = [rock,paper,scissors]

# Random Choice User
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n"))
print("User Choice: ")
print(game_images[user_input])

# Random Choice Computer
computer_input = random.randint(0, 2)
print("Computer Choice: ")
print(game_images[computer_input])

# Logic Rules
if user_input == 0 and computer_input == 2:

    print("You Lose!")
elif computer_input == 0 and user_input == 2:
    print("You Win!")
elif computer_input > user_input:
    print("You Lose!")
elif user_input > computer_input:
    print("You Win!")
elif user_input == computer_input:
    print("Its a Draw")
else:
    print("You Lose!")
