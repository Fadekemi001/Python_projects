from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

your_cards = random.sample(cards, k=2)

computer_card = random.sample(cards, k=2)

while input("Do you want to play Blackjack? Type 'y' or 'n': ") == "y":
    current_score = 0

    computer_score = 0

    print(logo)

    for num in your_cards:
        current_score += num


    for num in computer_card:
        computer_score += num

    while computer_score < 17:
       computer_card.append(random.choice( cards))
       computer_score = 0
       for num in computer_card:
           computer_score += num


    print(f"Your cards:{your_cards}, Current score : {current_score}\n Computer's first cards:{computer_card[0]}")

    hit = input("Type 'y' to get another card, type 'n' to pass:\n")
    while hit == "y":
        your_cards.append(random.choice( cards))
        current_score = 0
        for num in your_cards:
            current_score += num
        print(f"Your cards:{your_cards}, Current score : {current_score}")  # this will be a while loop
        hit = input("Type 'y' to get another card, type 'n' to pass:\n")
    print(f"Your final hand:{your_cards}, final score : {current_score}\n ")
    print(f"Computer cards:{computer_card}, Computer score : {computer_score}\n ")

    if current_score <21:
        if current_score >computer_score :
            print("You win!")
    elif current_score > 21:
        print("Bust! You lose!")
    elif current_score == 21:
        print("BlackJack!You win!")
    elif current_score == computer_score:
        print("Push!")
    else:
        print("You lose!")
input("Do you want to play Blackjack? Type 'y' or 'n': ")






