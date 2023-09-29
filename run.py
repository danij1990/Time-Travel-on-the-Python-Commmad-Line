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