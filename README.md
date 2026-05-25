# Tic Tac Toe - Python CLI Game

A simple command-line Tic Tac Toe game built in Python with a rule-based AI opponent.

## 🎮 Features

- Human vs AI gameplay
- Rule-based AI that prioritizes:
  - Winning moves
  - Blocking opponent wins
  - Center position
  - Corner positions
  - Random fallback move
- Win and draw detection
- Simple terminal-based interface

## 🧠 AI Logic

The AI follows a priority system:

1. Check if it can win in the current move
2. Block the opponent from winning
3. Take the center if available
4. Take a corner if available
5. Otherwise choose a random empty position

## 🛠️ Technologies Used

- Python 3
- Standard library only (`random`, `time`)
