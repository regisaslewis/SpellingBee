from spellingbee import spelling_bee, successful_words_used
from daily_letters import daily_letters
from all_answers import all_answers

copy = daily_letters().copy()
necessary_letter = copy[0]
optional_letters = copy[1:]


def main():
    print(f"Today's Letters: |{necessary_letter}| {optional_letters}")
    print("Press 0 to exit.")
    print("Press 1 to see your successful words.")
    points = 0
    while True:
        choice = input("Enter your word: ")
        if choice == "0":
            exit()
        elif choice == "1":
            print(sorted(successful_words_used))
        elif choice == "5742":
            all_answers(copy)
        else:
            message = spelling_bee(copy, choice)
            print(message)
            print("=============")
            if message == "Success!":
                points += 1 if len(choice) == 4 else len(choice)
                print(f"+{1 if len(choice) == 4 else len(choice)}")
                print(f"Total Points: {points}")
                print("=============")
            elif message == "!! PANGRAM !!":
                points += (len(choice) + 7)
                print(f"+{(len(choice) + 7)}")
                print(f"Total Points: {points}")
                print("=============")
            print(f"|{necessary_letter}| {optional_letters}")
        

if __name__ == "__main__":
    main()