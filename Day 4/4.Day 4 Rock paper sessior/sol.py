user_choice = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for scissors.\n"))
import random
computer_choice = random.randint(0, 2)
print(f"computer choose {computer_choice}")
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
if user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")        
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")    
elif user_choice == computer_choice:
    print("It's a draw")
elif user_choice >= 3 or user_choice < 0:
    print("you typed an invalid number. You lose!")    
else:
    print("you typed an invalid number. You lose!")
