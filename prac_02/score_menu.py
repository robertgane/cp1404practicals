def main():
    MENU_CHOICE = "(G)et score\n(D)isplay result\n(P)rint stars\n(Q)uit"
    score = get_valid_score()
    print(MENU_CHOICE)
    choice = input("> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "D":
            print(f"Your score is {score}")
        elif choice == "P":
            print("*" * score)
        else:
            print("Invalid Choice")
        print(MENU_CHOICE)
        choice = input("> ").upper()
    print("Goodbye")


def get_valid_score():
    score = int(input("Score: "))
    while score > 100 or score < 0:
        print("Invalid Score")
        score = int(input("Score: "))
    return score


main()
