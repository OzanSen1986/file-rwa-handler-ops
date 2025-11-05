import random
cards = ["Ace", "King", "Jack", "Joker"]


guess_list = []

def suffix(guess):
    if guess == 1:
        return "st"
    elif guess == 2:
        return "nd"
    elif guess == 3:
        return "rd"
    else:
        return "th"

try:
    guess = 1
    while guess <=3:
        selection = random.choice(cards)
        if selection == "Joker":
            print(f"You found Joker at {guess}{suffix(guess)} times.")
            guess_list.append(selection)
            break
        guess_list.append(selection)
        guess += 1
    else:
        print("You did not guess the joker at the allowed times.")
finally:
    print(f"Guessed list: {guess_list}")




