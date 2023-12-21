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

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)

rps = [rock, paper, scissors]

print(f"You chose:\n{rps[user_choice]}")
print(f"Computer chose:\n{rps[computer_choice]}")

if user_choice == 0 and computer_choice == 2:
    print("You Win!")
elif computer_choice > user_choice:
    print("You Lose!")
elif computer_choice == 0 and user_choice == 2:
    print("You Lose!")
elif computer_choice < user_choice:
    print("You Win!")
elif computer_choice == user_choice:
    print("Draw!")