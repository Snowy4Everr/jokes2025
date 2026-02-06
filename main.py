jokes = {
    "robbers": [
        "Knock Knock",
        "Calder",
        "Calder police — I've been robbed!"
    ],
    "tanks": [
        "Knock Knock",
        "Tank",
        "You're welcome!"
    ],
    "pencils": [
        "Knock Knock",
        "Broken pencil",
        "Nevermind — it's pointless!"
    ]
}

def tell_joke(category):
    if category in jokes and len(jokes[category]) > 0:
        for line in jokes[category]:
            input(line + " ")
        jokes.pop(category)  # modifies the list of available jokes
    else:
        print("That joke has already been told or does not exist.")

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

    while start == "yes" and len(jokes) > 0:
        print("Available jokes:", ", ".join(jokes.keys()))
        choice = input("Choose a joke type: ").lower()

        tell_joke(choice)
        start = ask_continue()

    print("No more jokes left!")
    rate_game()

main()
