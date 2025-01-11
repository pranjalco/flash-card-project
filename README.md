# Project 21: Flash Card Project

## Author
- **Name**: Pranjal Sarnaik
- **Date**: 01 Jan 2025

## Description:
The Flash Card Project is designed to help users learn new languages effectively. The application displays a flashcard with a French word on the front and its English translation on the back. Every 3 seconds, the card flips to show the other side. Users can interact with the app using two buttons: “Right” and “Wrong”.

### Features:
- **Dynamic Flashcards**: Learn new words with randomized cards.
- **Progress Tracking**: Correctly learned words are removed from the word list and saved to a separate file.
- **Error Handling**: Uses a `try: except` block to handle file reading issues.
- **Restart Option**: Prompts the user to play again once all words are learned.

## How to Use:
1. When the program starts, a card with a French word appears.
2. After 3 seconds, the card flips to reveal the English translation.
3. Use the **Right** button if you’ve learned the word, removing it from the word list and saving progress.
4. Use the **Wrong** button to see the word again in the future.
5. Once all words are learned, the program asks if you’d like to restart.

## Level
- **Level**: Intermediate
- **Skills**:Python Programming, Tkinter GUI Development, File Handling with Pandas, Error Handling in Python
- **Domain**: Language Learning

## Features
- Interactive and user-friendly GUI.
- Tracks progress by saving unlearned words to `wants_to_learn.csv`.
- Randomized word selection for varied learning experience.
- Handles missing or incomplete files gracefully.

## Installation

### Prerequisites:
1. Python 3.9 or later installed on your system.
2. Modules used:
   - `tkinter`
   - `pandas`
   - `random`
   - `os`

### Steps:
1. Clone this repository:
   ```bash
   git clone https://github.com/pranjalco/flash-card-project.git
   ```

2. Navigate to the project directory:
   ```bash
   cd flash-card-project
   ```

3. Install required dependencies (if not already installed):
   ```bash
   pip install pandas
   ```

## Running the Program
1. Open the project directory in your terminal or IDE.
2. Execute the program:
   - **Using PyCharm**: Open the project and run `app.py`.
   - **Using Terminal/Command Prompt**: Navigate to the project folder and run:
     ```bash
     python app.py
     ```
   - **By Double-Clicking**: Run `app.py` directly (if Python is set up to execute `.py` files).

3. Enjoy learning French vocabulary interactively!

## File Structure:
```
flash-card-project/
├── app.py                # Main application file
├── data/                # Folder for .csv files
│   └── french_words.csv    # Original word list
│   └── wants_to_learn.csv   # Updated word list
├── images/              # Images for cards and buttons
├── screenshots/         # Screenshots of the application
├── experiments/         # Temporary or practice files
└── README.md           # Project documentation
```

---
**Created by Pranjal Sarnaik**  
*© 2024. All rights reserved.*

