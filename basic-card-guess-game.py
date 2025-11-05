import random
cards = ["Ace", "King", "Jack", "Joker"]


guess_list = []

def suffix(sfx):
    match sfx:
        case 1:
            return "st"
        case 2:
            return "nd"
        case 3:
            return "rd"
        case _:
            return "th"
        
      
def guess_card():
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

def main():
    guess_card()
    
if __name__ == "__main__":
    main()

