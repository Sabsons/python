from art import logo
import random

gameloop = True
play = True


# Create deck and return random card.
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards_list):
    if len(cards_list) == 2 and 11 in cards_list and 10 in cards_list:
        return 0
    if 11 in cards_list and sum(cards_list) > 21:
        cards_list.remove(11)
        cards_list.append(1)
    return sum(cards_list)


# Compare the scores
def compare(user_score, computer_score):
    if user_score == computer_score:
        print("Draw")

    if computer_score == 0:
        print("You lose")

    if user_score == 0:
        print("You win")

    if user_score > 21:
        print("You lose")

    if computer_score > 21:
        print("You win")

    if computer_score > user_score and computer_score < 21:
        print("You lose")

    if user_score == 21:
        print("You win")

    if computer_score == 21:
        print("You lose")


while play:
    player_continue = input("Do you want to play a game of blackjack? y/n ")
    if player_continue[0].lower() == "n":
        play = False
    else:
        print(logo)
        # Give two random cards for the user and the computer by adding to the list the deal_card function two times.
        user_cards = [deal_card(), deal_card()]
        computer_cards = [deal_card(), deal_card()]
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your cards: {user_cards} , current score: {user_score}")
        print(f"    Computer's first card is: {computer_cards[0]}")
        gameloop = True
        while gameloop:

            if user_score == 0 or user_score > 21 or user_score == 21:
                compare(user_score, computer_score)
                gameloop = False
                break
            elif computer_score == 0 or computer_score > 21 or computer_score == 21:
                compare(user_score, computer_score)
                gameloop = False
                break
            else:
                decision = input("Type 'y' to draw another card, 'n' to pass: ")
                if decision.lower() == "y":
                    user_cards.append(deal_card())
                    user_score = calculate_score(user_cards)
                    print(f"    Your cards: {user_cards}, current score {user_score}")
                    print(f"    Computer's first card is: {computer_cards[0]}")

                # Give enough cards to computer player so that his score is above the user's score.
                if decision.lower() == "n":
                    while computer_score < 17:
                        computer_cards.append(deal_card())
                        computer_score = calculate_score(computer_cards)
                    print(f"Your final hand is {user_cards}, final_score: {user_score}")
                    print(f"The computer final hand is {computer_cards} and score is {computer_score}")
                    compare(user_score, computer_score)
                    gameloop = False
