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
user_input = int(input("What do zou choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_input == 0:
    print("Your choice:")
    print(rock)
elif user_input ==1:
    print("Your choice:")
    print(paper)
elif user_input == 2:
    print("Your choice:")
    print(scissors)
else:
    print("Your input is invalid! Start again!")
    exit()
import random
computer_choice = random.randint(0, 2)
if computer_choice == 0:
    print("Computer chose:")
    print(rock)
elif computer_choice ==1:
    print("Computer chose:")
    print(paper)
elif computer_choice == 2:
    print("Computer chose:")
    print(scissors)

if user_input == 0 and computer_choice == 0:
    print("It's draw! Try again!")
elif user_input == 0 and computer_choice == 1:
    print("You lose!")
elif user_input == 0 and computer_choice == 2:
    print("You win!")

if user_input == 1 and computer_choice == 0:
    print("You win!")
elif user_input == 1 and computer_choice == 1:
    print("It's draw! Try again!")
elif user_input == 1 and computer_choice == 2:
    print("You lose!")

if user_input == 2 and computer_choice == 0:
    print("You lose!")
elif user_input == 2 and computer_choice == 1:
    print("You win!")
elif user_input == 2 and computer_choice == 2:
    print("It's draw! Try again!")
