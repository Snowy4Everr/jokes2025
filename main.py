

joketypes = ["robbers", "tanks", "pencils"]
# make this performance task ready for submission
# To give the user a fun experience hearing knock knock jokes







# Knock-Knock Joke Program (Refactored)
# Includes lists, functions, parameters, abstraction, sequencing, selection, iteration

# A list storing joke categories


def tell_joke(category):
    if category == "robbers":
        input("Knock Knock ")
        input("Calder ")
        print("Calder police — I've been robbed!")
    elif category == "tanks":
        input("Knock Knock ")
        input("Tank ")
        print("You're welcome!")
    elif category == "pencils":
        input("Knock Knock ")
        input("Broken pencil ")
        print("Nevermind — it's pointless!")

def ask_continue():
    return input("Do you want to hear another joke? (yes/no) ").lower()

def rate_game():
    rating = int(input("Please rate our game 1–10: "))
    score = rating * 10
    print(str(score) + "% satisfaction rate")
    recommend = input("Would you recommend this game to a friend? ").lower()
    if recommend in ["yes", "maybe"]:
        print("Thanks, we appreciate it!")
    else:
        print("Sorry you did not enjoy it.")

def main():
    start = input("Do you want to hear a joke? (yes/no) ").lower()

    if start == "no":
        print("Okay, suit yourself!")
        return

    while start == "yes":
        print("Great! Let's play.")
        choice = input("Choose a joke: robbers, tanks, or pencils: ").lower()

        if choice in joketypes:
            tell_joke(choice)
        else:
            print("That is not a valid joke type.")

        start = ask_continue()

    rate_game()

main()