# Flashy: Language Learning App

## Description
A graphical flashcard application designed to help users memorize vocabulary. Built with Tkinter, it currently assists in learning Arabic words by displaying flashcards that automatically flip to reveal translations.

## Features
- Interactive graphical user interface (GUI) with Tkinter.
- Auto-flipping cards (flips after 3 seconds).
- Tracks known words: clicking the checkmark removes the word from the learning pool.
- Automatically saves progress to a CSV file so you can resume learning later.

## Technologies
- Python 3.x
- 	kinter for the GUI.
- pandas for reading, updating, and writing CSV data.

## Installation
1. Clone the repository:
   `ash
   git clone https://github.com/yourusername/flashcard-app.git
   cd flashcard-app
   `
2. Install the required dependencies:
   `ash
   pip install -r requirements.txt
   `

## Usage
Start the application:
`ash
python main.py
`
- Click the **✓** button if you knew the word. It won't be shown again.
- Click the **✗** button if you didn't know the word. It remains in the deck.

## Project Structure
- main.py: The main GUI application.
- data/: Contains the initial and progress CSV files.
- images/: Contains UI assets (card fronts, backs, buttons).

## Requirements
- Python 3.9+
- See 
equirements.txt for specific library versions.

## Future Improvements
- Support for multiple languages and custom decks.
- Add audio pronunciation for the words.
- Implement a spaced repetition algorithm (SRS).

## License
This project is licensed under the MIT License.