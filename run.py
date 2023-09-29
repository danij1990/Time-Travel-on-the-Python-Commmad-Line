import random  # Importing the random module for generating random choices


# Function for the main time travel game
def time_travel():
    # Printing welcome and instructions
    print("Welcome to the Time Travel Game!")
    print("You find yourself in a mysterious time machine.")
    print("You need to answer all the questions and riddles")
    print("to escape the time warp.")
    print("Try to escape the loop and also have fun.")

    # Flag to track if all questions are answered
    answered_all_questions = False

    # Loop to play the game until all questions are answered
    while not answered_all_questions:
        options = {
            1: "Go to the future",
            2: "Go back in time",
            3: "Stay in the present day",
            4: "Your Birthday, but which one?"
        }
        for key, value in options.items():
            print(f"{key}: {value}")

        choice = input("Enter your choice: ")

        # Checking the user's choice and calling corresponding functions
        if choice == '1':
            print("You have landed on a spaceship.")
            explore_future()
        elif choice == '2':
            print("You venture deeper into the forest and encounter a wild animal.")
            encounter_past()
        elif choice == '3':
            print("You are whisked off to a mountain range.")
            today()
        elif choice == '4':
            print("You have landed at your 90th birthday party.")
            your_birthday()
        else:
            print("Invalid choice. Please try again.")

    # Printing congratulations when the game is completed
    print("Congratulations! You have answered all the questions and completed the game.")


# Function to explore the future
def explore_future():
    print("You find a safe on the spaceship.")
    print("Do you want to open the safe?")
    print("A. Yes")
    print("B. No")
    print("C. Continue to search")

    choice = input("Enter your choice (A/B/C): ")

    if choice.lower() == 'a':
        if ask_question1("What goes up but must come down?", "A"):
            print("Congratulations! You found a valuable treasure.")
        else:
            print("You answered the riddle incorrectly. Game over.")
    elif choice.lower() == 'b':
        print("You leave the cave and continue your time-traveling adventure.")
    elif choice.lower() == 'c':
        print("You found an old, dusty book. It has some interesting ancient stories.")
    else:
        print("Invalid choice. Please try again.")


# Function to encounter the past
def encounter_past():
    print("You have landed beside a fierce dinosaur!")
    print("What do you want to do?")
    print("A. Fight the animal")
    print("B. Try to run away")

    choice = input("Enter your choice (A/B): ")

    if choice.lower() == 'a':
        if ask_question2("What belongs to you, but other people use it more than you do?", "B"):
            print("You fought the animal and managed to defeat it.")
        else:
            print("You answered the riddle incorrectly. Game over.")
    elif choice.lower() == 'b':
        print("You try to run away, but the animal catches you.")
        print("Game over. You were not able to escape.")


# Function for the "stay in the present day" option
def today():
    print("You are near the top of a mountain!")
    print("What do you want to do?")
    print("A. Keep Climbing")
    print("B. Try to run away")

    choice = input("Enter your choice (A/B): ")

    if choice.lower() == 'a':
        if ask_question3("What is the world's largest mountain?", "A"):
            print("You reached the top of Everest.")
        else:
            print("You answered the riddle incorrectly. Game over.")
    elif choice.lower() == 'b':
        print("You had to be rescued by the locals.")
        print("Game over. You were not able to escape.")


# Function for the "your birthday" option
def your_birthday():
    print("Would you rather")
    print("A. Stay at the party?")
    print("B. Choose to return home?")

    choice = input("Enter your choice (A/B): ")

    if choice.lower() == 'a':
        if ask_question4("What has keys but can't open locks?", "B"):
            print("Enjoy your party.")
        else:
            print("You answered the riddle incorrectly. Game over.")
    elif choice.lower() == 'b':
        print("The party is over.")
        print("Game over. You were not able to escape.")


# Question function 1 to ask a question with multiple choices
def ask_question1(question, correct_choice):
    print(question)
    print("Choices:")
    print("A. A Plane")
    print("B. A Cat")
    print("C. A Dog")
    user_choice = input("Your choice (A/B/C): ").lower()
    return user_choice == correct_choice.lower()


# Question function 2 to ask a question with multiple choices
def ask_question2(question, correct_choice):
    print(question)
    print("Choices:")
    print("A. Your Heart")
    print("B. Your Name")
    print("C. Your Money")
    user_choice = input("Your choice (A/B/C): ").lower()
    return user_choice == correct_choice.lower()


# Question function 3 to ask a question with multiple choices
def ask_question3(question, correct_choice):
    print(question)
    print("Choices:")
    print("A. Everest")
    print("B. K2")
    print("C. Mount Fuji")
    user_choice = input("Your choice (A/B/C): ").lower()
    return user_choice == correct_choice.lower()


# Question function 4 to ask a question with multiple choices
def ask_question4(question, correct_choice):
    print(question)
    print("Choices:")
    print("A. Map")
    print("B. Piano")
    print("C. Glasses")
    user_choice = input("Your choice (A/B/C): ").lower()
    return user_choice == correct_choice.lower()


if __name__ == "__main__":
    time_travel()
