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
scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

element = [rock, paper, scissor]


okay = random.randint(0, 2)


you = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissor.\n"))

if you in [0, 1, 2]:
    print("You chose:")
    print(element[you])

    print("Computer chose:")
    print(element[okay])

    if you == okay:
        print("It's a draw!")
    elif (you == 0 and okay == 2) or (you == 1 and okay == 0) or (you == 2 and okay == 1):
        print("You win!")
    elif you == okay :
        print("It's a Draw!!")    
    else:
        print("Computer wins!")
else:
    print("You haven't entered a valid number (0, 1, or 2)")
  

