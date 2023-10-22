import random
# import pyfiglet module 
import pyfiglet 

result = pyfiglet.figlet_format("Time Travel", font = "digital" ) 
print(result) 

name = input("Enter your name: ")

# Validate and get a valid age
while True:
    age = input("Enter your age: ")

    if age.isdigit():
        age = int(age)
        break
    else:
        print("Please enter a valid number for age.")

print(f"Hello {name}! You are {age} years old.")


# Function to ask a question with multiple choices
def ask_question(question, choices, correct_choice):
    print(question)
    for i, choice in enumerate(choices, start=1):
        print(f"{chr(64 + i)}. {choice}")

    user_choice = input("Your choice (A/B/C/D): ").upper()
    return user_choice == correct_choice


# Function for the main time travel game
def time_travel():
    print("Welcome to the Time Travel Game!")
    print("You find yourself in a mysterious time machine.")
    print("You need to answer all the questions and riddles")
    print("to escape the time warp.")
    print("Try to escape the loop and also have fun.")

    questions = [
        {
            "question": "What goes up but must come down?",
            "choices": ["A Plane", "A Cat", "A Dog", "A Balloon"],
            "correct_choice": "A",
            "adventure_route": "You see a time portal resembling a floating airplane. You board it and embark on a journey to a futuristic city."
        },
        {
            "question": "What belongs to you, but other people use it more than you do?",
            "choices": ["Your Heart", "Your Name", "Your Money", "Your House"],
            "correct_choice": "B",
            "adventure_route": "You notice a time portal leading to your house. As you enter, you find a hidden treasure in your backyard."
        },
        {
            "question": "What is the world's largest mountain?",
            "choices": ["Everest", "K2", "Mount Fuji", "Makalu"],
            "correct_choice": "A",
            "adventure_route": "You spot a time portal leading to the highest peak. You climb and discover a hidden cave with ancient artifacts."
        },
        {
            "question": "What has keys but can't open locks?",
            "choices": ["Map", "Piano", "Glasses", "Cryptography"],
            "correct_choice": "B",
            "adventure_route": "You come across a time portal resembling a grand piano. As you approach, the piano door opens, revealing a room with a treasure chest."
        },
        {
            "question": "What is always in front of you but can't be seen?",
            "choices": ["The Future", "The Past", "The Present", "Your Nose"],
            "correct_choice": "C",
            "adventure_route": "You find a time portal surrounded by mist. As you walk through it, you enter a hidden garden full of wonders."
        }
    ]

    # List to track if each question is answered correctly
    correct_answers = [False] * len(questions)

    # Loop to play the game
    while not all(correct_answers):
        for i, question_info in enumerate(questions, start=1):
            print(f"\nYou encounter a time portal that reads: '{question_info['adventure_route']}'")
            print(f"What do you want to do for question {i}?")
            print("A. Continue, Answers the questions to beat the portal ")
            print("B. Try to escape, but risk getting stuck")
            
            portal_choice = input("Your choice (A/B): ").upper()

            if portal_choice == 'A':
                correct_answers[i-1] = ask_question(question_info["question"], question_info["choices"], question_info["correct_choice"])

                # If the answer is wrong, end the game and start over
                if not correct_answers[i-1]:
                    print("Oops! You answered incorrectly. Starting over.")
                    break

            elif portal_choice == 'B':
                print("You are stuck in the portal, Game over.")
                return

            else:
                print("Invalid choice. Game over.")
                return

    # Printing congratulations when the game is completed
    print("You have escaped the loop! Well done!")


if __name__ == "__main__":
    time_travel()