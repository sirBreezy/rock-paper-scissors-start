# 100 Day Challenge - Day 4
# Rock, Paper, Scissors text game
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
images = [rock, paper, scissors]
print("Let's play a game of Rock, Paper, Scissors!")
choice = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors.\n:"))
print(images[choice])
computer_choice = random.randint(0, 2)
print("Computer chose: ")
print(images[computer_choice])
if choice >= 3 or choice < 0:
  print("You chose an invalid number, you lose!")
elif choice == 0 and computer_choice == 2:
  print("You win!")
elif choice < computer_choice:
  print("You lose!")
elif choice > computer_choice:
  print("You win!")
elif choice == computer_choice:
  print("It's a draw!")
 


