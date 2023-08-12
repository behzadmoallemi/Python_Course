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
game_images = [rock, papers, scissors]

user_input = int(input("What do zou choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))


if user_input == 0 or user_input == 1 or user_input == 2:
    print(f"Your choice:{game_images[user_input]}")
else:
    print("Your input is invalid! Start again!")
    exit()
import random
computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])


result = str(user_input) + str(computer_choice)



if result == "00" or result == "11" or result == "22" :
    print("It's draw! Try again!")
elif result == "10" or result == "02" or result == "21" :
    print("You wine!")
elif  result == "01" or result == "20" or result == "12" :
    print("You lose!")
