import random

allcards = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 2,
    "Q": 3,
    "K": 4,
    "A": 11,
}


def deal_card():
    cards = list(allcards.keys())
    return random.choice(cards)


def calculate_score(cards):
    score = sum(allcards[card] for card in cards)
    if score == 21 and len(cards) == 2:
        return 0  # "Blackjack!"
    if "A" in cards and score > 21:
        score -= 10
    return score


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "Draw!"
    if user_score == computer_score:
        return "Draw!"
    elif computer_score == 0:
        return "You lose! PC have Blackjack"
    elif user_score == 0:
        return "You won! you have Blackjack"
    elif user_score > 21:
        return "You lose! You have more than 21 points"
    elif computer_score > 21:
        return "You won! PC have more than 21 points"
    elif user_score > computer_score:
        return "You won!"
    else:
        return "You lose!"


def play_game():
    print("Welcome'!")

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, your score: {user_score}")
        print(f"PC cards: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            should_continue = input("Take one more card? 'y' або 'n': ")
            if should_continue == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # комп у нас ризикований хлоп, завжди надіється якщо балів менше 19 взяти двійку
    while computer_score != 0 and computer_score <= 19:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your cards: {user_cards}, your score: {user_score}")
    print(f"PC cards: {computer_cards}, pc score: {computer_score}")
    print(compare(user_score, computer_score))


play_game()
