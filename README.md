# Sudoku Solver

(SEE THE USAGE SECTION TO GENERATE A VALID INPUT)

## Overview
This Sudoku Solver is a Python project using Constraint Propagation to 
efficiently solve simple Sudoku puzzles.

1st completed project.

## Features
- Constraint propagation: systematic elimination of possibilities through two Sudoku strategies (hidden & naked singles).
- Utilizes a NumPy 2-d array to represent & navigate the board.
- Users input their own Sudoku grid to solve.
- (Tested on Windows only.)

## Limitations
Constraint propagation: puzzles requiring unimplemented Sudoku strategies cannot be solved. For example: X-Wing, Swordfish, etc.

## Requirements
- numpy==1.26.4

## Usage:
1. Clone the repository to your machine
2. Navigate to the project directory
3. Create a venv: "python -m venv venv"
4. Activate the venv: "venv\Scripts\activate"
5. Install the required package: "pip install -r requirements.txt"
6. Run "sudoku.py"
7. To generate a valid input, use the following: https://qqwing.com/generate.html with a "One line" output format.
   The puzzle must contain only Givens, Singles and Hidden Singles.
   Input example: ..13....7..........7..142.3.5...1......96...2...2..139.65....2.........41..7..596

## Keywords:
- Sudoku
- Constraint propagation
- NumPy