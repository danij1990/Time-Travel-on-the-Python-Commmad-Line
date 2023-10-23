# Time Travel on the Python Commmad Line 



## Time Travel Adventure Game Overview

Welcome to the "Time Travel Adventure Game," an exciting text-based adventure that takes you on a journey through time and challenges your wits. In this game, you'll find yourself inside a mysterious time machine, facing a series of questions and riddles. Your mission is to answer them correctly and navigate through time portals to escape the time warp.

## Key Features

### 1. Time Travel Theme

- Immerse yourself in a time travel-themed adventure, where you encounter time portals leading to different eras and destinations.
- Explore a variety of time periods and unlock thrilling adventures in each.

### 2. Interactive Storytelling

- Engage in an interactive storyline that unfolds with each question you answer.
- Your choices determine the outcome of your adventure, adding an element of decision-making and suspense to the game.

### 3. Challenging Questions and Riddles

- Test your knowledge and critical thinking with a series of intriguing questions and riddles.
- Each question has multiple-choice answers, and you must select the correct one to progress.

### 4. Escape the Loop

- Your ultimate goal is to escape the time loop. To achieve this, you must successfully answer all questions and overcome the challenges posed by the time portals.
- Wrong answers may lead to starting over, so choose wisely!

### 5. Player Interaction

- Enter your name and age to personalize your gaming experience.
- Make choices during the game that affect the direction of your adventure.

### 6. Exciting Adventure Routes

- Explore various adventure routes associated with each question.
- These routes include futuristic cities, hidden treasures, ancient artifacts, and hidden gardens.

### 7. Game Progress Tracking

- Keep track of your progress as you answer questions correctly or face challenges.
- The game's logic ensures you only escape the loop once you've conquered all the obstacles.

### 8. Replayability

- With multiple questions and adventure routes, the game offers high replayability. Try different routes and challenge yourself to answer all questions correctly.

### 9. Enjoyable and Educational

- Have fun while expanding your knowledge and problem-solving skills.
- The game combines entertainment with a mental challenge, making it suitable for players of all ages.

### 10. Author Interaction

- If you have questions or need assistance, the game's author is available for support and feedback.

The "Time Travel Adventure Game" offers a captivating blend of time travel, puzzles, and decision-making, providing an enjoyable and immersive gaming experience. Embark on this adventure, answer the questions, and see if you can escape the time loop. Good luck, time traveler!

**Join Us:**

Ready to embark on an exciting journey through time? Join the Time Travel on the Python Commmad Line community and become a part of our time-traveling adventure!

How to Get Involved
Contribute to the Codebase: If you're passionate about game development, Python programming, or have creative ideas to enhance the gameplay, consider contributing to our open-source project on GitHub. Your contributions are highly valued!

Fork the repository: Time-Travel-on-the-Python-Commmad-Line
Make your improvements and enhancements.
Submit a pull request to share your changes with the community.
Report Bugs and Issues: Encountered a bug or have a suggestion for improvement? Let us know by opening an issue on GitHub. Your feedback helps us make the game better!

Open a New Issue
Spread the Word: Share the Time-Travel-on-the-Python-Commmad-Line with your friends, family, and fellow gamers! Help us grow our community and bring more adventurers into the time-traveling fold.

Tweet about the game: Time Travel on the Python Commmad Line
### Flowchart

![Flowchart](assets/images/Flowchart.png)

# Time Travel on the Python Commmad Line

## Description



## How to Play the Time Travel Game

The "Time Travel Game" is an interactive text-based adventure where you embark on a time-traveling journey filled with questions and riddles. Follow these steps to play the game and experience the adventure:

1. **Prerequisites**: Make sure you have Python installed on your computer. You can download Python from [python.org](https://www.python.org/downloads/) if it's not already installed.

2. **Clone or Download**: Clone the game repository to your local machine or download the game script from the repository.

   ```shell
   git clone https://github.com/Time-Travel-on-the-Python-Commmad-Line
   ```

3. **Navigate to the Game Directory**: Open your command prompt or terminal and change your working directory to the folder where the game script is located.

   ```shell
   cd Time-Travel-on-the-Python-Commmad-Line
   ```

4. **Start the Game**: Run the game script by executing the following command:

   ```shell
   python run.py
   ```

5. **Initial Input**: The game will start by displaying a stylish title and prompt you to enter your name. Type your name and press "Enter."

6. **Age Validation**: You will then be prompted to enter your age. Make sure to enter a valid age (a positive integer). The game will ensure that your input is a valid number.

7. **Game Introduction**: After entering your name and age, the game will welcome you to the Time Travel adventure. You'll be presented with a time machine and a series of mysterious time portals.

8. **Answer Questions and Make Choices**: Your objective is to answer questions correctly to progress in the game. When you encounter a time portal, you have two choices:
   - **A. Continue**: Choose to continue your adventure and answer the question associated with the portal. If you answer correctly, you advance in the game.
   - **B. Try to Escape**: Choose to escape the portal. Be cautious, as escaping may come with consequences!

9. **Completing the Game**: Continue to answer questions, make choices, and explore the time portals. Your goal is to answer all questions correctly and navigate through the portals to reach the end of the adventure. When you successfully complete the game, you will receive a congratulatory message.

10. **Replay the Game**: If you'd like to replay the game, simply run the script again, and the adventure will start over.

Enjoy the "Time Travel Game" and have fun solving riddles, making choices, and escaping the time warp. Explore the various outcomes and see if you can conquer the time-travel adventure. If you encounter any issues or have feedback, please feel free to share it with us through the repository's issue tracker.
```

This "How to Play" section provides users with a step-by-step guide on how to start and enjoy your game, making it easy for them to understand the gameplay mechanics and objectives.
## Apps Used

| App           | Description                |
| ------------- | -------------------------- |
| Git           | Version control system     |
| GitHub        | Code hosting platform      |
| CodeAnywhere  | Online code editor         |
| Heroku        | Deployment platform        |



## Getting Started




## Testing the Time Travel Game

To ensure the "Time Travel Game" functions as intended, several tests were conducted to verify its correctness and robustness. Here are the test scenarios and their outcomes:

### 1. User Input Validation

**Scenario**: Ensure that the game correctly validates user input for name and age.

**Test Steps**:
1. Run the game and enter a valid name.
2. Enter a non-integer value for age.
3. Verify that the game prompts for a valid age.
4. Enter a valid age.

**Outcome**: The game should accept valid inputs and reject invalid ones, proceeding only when valid data is provided.

### 2. Question-Answer Mechanism

**Scenario**: Confirm that the game presents questions and checks answers.

**Test Steps**:
1. Play the game, ensuring that questions are presented.
2. Answer all questions correctly.
3. Answer at least one question incorrectly.

**Outcome**: The game should continue when questions are answered correctly and restart when an incorrect answer is given.

### 3. Time Portal Choices

**Scenario**: Test the choices presented when encountering time portals.

**Test Steps**:
1. Play the game and reach a time portal.
2. Choose to continue and answer the question correctly.
3. Choose to continue and answer the question incorrectly.
4. Choose to escape the time portal.

**Outcome**: The game should respond appropriately to each choice, progressing when questions are answered correctly, restarting on incorrect answers, and ending when choosing to escape.

### 4. Game Completion

**Scenario**: Verify the game's completion when all questions are answered correctly.

**Test Steps**:
1. Play the game and answer all questions correctly.

**Outcome**: The game should provide a "Congratulations" message and indicate successful completion.

### 5. Error Handling

**Scenario**: Test the game's response to unexpected input.

**Test Steps**:
1. Play the game and provide invalid choices or inputs.

**Outcome**: The game should gracefully handle invalid input and display appropriate error messages.

### 6. Replayability

**Scenario**: Test the game's ability to restart and allow replay.

**Test Steps**:
1. Complete the game successfully.
2. Choose to replay the game.

**Outcome**: The game should restart, allowing users to play again.

### 7. Performance and Resource Usage

**Scenario**: Assess the game's performance and resource usage.

**Test Steps**:
1. Monitor the game's resource consumption while playing.
2. Verify that the game runs smoothly without significant resource utilization.

**Outcome**: The game should run without performance issues and use system resources efficiently.

These tests were conducted to ensure the "Time Travel Game" works correctly and provides an engaging experience for players. If you encounter any issues or have suggestions for improvements, please feel free to submit them to the repository's issue tracker.



### Test Results 



### Technologies Used



### Key Features



### Development Process


## Deployment

### Version Control
The site was created using Codeanywhere code editor and pushed to github to the remote repository ‘Time-Travel-on-the-Python-Commmad-Line’.

The following git commands were used throughout development to push code to the remote repo:

```git add <file>``` - This command was used to add the file(s) to the staging area before they are committed.

```git commit -m “commit message”``` - This command was used to commit changes to the local repository queue ready for the final step.

```git push``` - This command was used to push all committed code to the remote repository on github.
### Deployment to 

### Clone the Repository 



## Future Development



## Acknowledgments

Special thanks to:

- [Geek for Geeks](https://www.geeksforgeeks.org/) for the `pyfiglet` module.
- [Jamie O'Neill](https://www.linkedin.com/in/jamie2023/) (Code Institute cohort lead) for 
- [Mentimeter](https://www.mentimeter.com) for more exciting quiz and interactive content!
- [Freecodecamp.org](https://www.youtube.com/watch?v=rfscVS0vtbw&t=2305s) This video greatly improved my understanding of Python.



## Bugs



## Contact

Daniel Hughes, Mullingar Co Westmeath, Ireland.

Phone : +353 852570069

Email : danijhughes@gmail.com

Git Hub : danij1990

Linkedin: <https://www.linkedin.com/in/daniel-hughes-36a948258/>

Facebook: <https://www.facebook.com/danny.hughes.96558>