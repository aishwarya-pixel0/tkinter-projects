# Tkinter-projects
## 1. Flash Card
This is a Python-based flash card application to help users learn French vocabulary. The app displays French words and their English translations using interactive flash cards.

How it Works ? 
* The app loads French words from a CSV file.
* Users view each word in french, try to recall its meaning, and then flip the card to see the english translation.
* Users can mark words as learned or skip them.
* Progress is saved in a separate CSV file, allowing users to continue learning where they left off.

 Here is a demo video : 

![Flash Card](https://github.com/user-attachments/assets/96d1966a-675b-4b11-b053-180c28222550)

## 2. Indian States and UTs Quiz Game

This project is a Python-based interactive quiz game that helps users learn and test their knowledge of the states and union territories (UTs) of India. The game uses a graphical map and sound effects to create an engaging learning experience.

How it Works ?
* The program loads `states_and_uts.csv` using pandas, which contains the names and coordinates of all Indian states and union territories.
* The game will display a map and prompt you to enter the names of Indian states and UTs.
* Correct answers are marked on the map and play a sound.
* Incorrect answers play a different sound.
* When the game ends, a message box displays the user's final score.
* The missed states/UTs are saved to `states_missed.csv` for further study.

Here is a demo video : 

![Indian Map](https://github.com/user-attachments/assets/b2eca868-a996-4083-9c62-66bbcd402423)

## 3. Miles to Kilometer Converter
Its main purpose is to help users convert distances from miles to kilometers using a user-friendly interface.

How It Works:
* The user enters a number representing miles.
* Upon clicking the "Convert" button, the application multiplies the input by 1.60934 (the conversion factor from miles to kilometers).
* The result is shown in the output field or label.

## 4.Pomodoro Timer
This project is a Pomodoro timer application built using Python and Tkinter. The Pomodoro Technique is a time management method that uses a timer to break work into intervals, typically 25 minutes in length, separated by short breaks. The application features a graphical user interface (GUI) that allows users to start, pause, and reset the timer, visually track work and break sessions, and stay focused and productive.

How it Works ?
* You can start the timer by clicking a button. The timer counts down a work session (usually 25 minutes).
* When the work session ends, the app automatically switches to a short break (typically 5 minutes), and the timer resets for the break.
* After the break, the app switches back to a work session. This cycle repeats, helping you alternate between focused work and rest.
* The app may track the number of completed Pomodoros (work sessions) and display progress.
* You can pause or reset the timer at any time using the provided controls.

Screenshots : 

<img width="300" height="400" alt="Screenshot (198)" src="https://github.com/user-attachments/assets/b142a743-f4f0-4136-91b4-dde3911678dc" />
<img width="300" height="450" alt="Screenshot (199)" src="https://github.com/user-attachments/assets/1394f798-87df-4640-9a5b-2a1e2c232b47" />


## 5.Quizzler
This project is a desktop quiz application built using Python and the Tkinter GUI library. It presents users with a series of true/false questions, tracks their score, and provides immediate feedback on their answers.

How it Works ?
* A question appears on the screen.
* You click True or False to answer.
* The app tells you if you’re right or wrong, updates your score, and shows the next question.
* This repeats until all questions are done.
* At the end, your final score is displayed

Here's a demo video : 

![Quizzler](https://github.com/user-attachments/assets/fe6e24b4-fbc1-41f7-b83e-85a3910f5455)

## 6.Snake Game
This project is a classic Snake Game implemented in Python using the Tkinter-based turtle graphics library. The player controls a snake that moves around the screen, eating food to grow longer and increase their score. The game features collision detection with the walls and the snake's own body, a scoreboard that tracks the current and high scores, and sound effects for scoring and game over events.

How it Works ?
* The game window opens and shows a snake, food, and your score.
* Use the arrow keys to move the snake.
* When the snake eats the food, it gets longer and your score goes up.
* If the snake hits the wall or itself, the game resets and your score starts over.
* The highest score is saved and shown at the top.
* Play as many times as you want until you close the window.






