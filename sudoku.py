"""
Implement a Sudoku solver program in Python. 

Your program should take an input Sudoku grid, either partially filled or completely empty, and determine a solution by filling in the missing digits while adhering to the Sudoku rules.

Your Sudoku solver program should have the following features:

    Input: Accept a 9x9 grid as input, either through user input or by reading from a file. The grid should represent the Sudoku puzzle, with empty cells represented by a dash ("-") or any other appropriate symbol.

    Solve: Implement an algorithm that solves the Sudoku puzzle and fills in the missing digits. The algorithm should use a combination of logical deduction techniques, such as elimination, unique candidate, subset, and "what if" analysis, to determine the correct values for each cell.

    Output: Display the solved Sudoku grid as output, with all cells filled in with the correct digits. Print the grid in a visually appealing format that is easy to read and understand.

    Error Handling: Handle invalid input gracefully. If the provided Sudoku grid is not valid (e.g., violates the Sudoku rules), display an appropriate error message.

    Multiple Solutions: Account for the possibility of puzzles having multiple valid solutions. If the puzzle has more than one valid solution, your program can display one of the solutions or indicate that the puzzle has multiple solutions.

Implement your Sudoku solver using appropriate data structures, algorithms, and programming techniques. You can choose to use any approach you prefer, such as backtracking, constraint propagation, or other methods.
"""

# My initial solution used backtracking only, which solved most puzzles
# almost instantly, even with relatively few clues.
# However, puzzles with few clues that were stacked at the end or certain
# digit orders (e.g 9-8-7-6-5-4-3-2-1 on the first line) took way too long.

# Instead, I rewrote the program using constraint propagation. I implemented
# only two strategies (naked and hidden singles) therefore it cannot solve
# every puzzle, but relatively simple ones do just fine.

# A simple "improvement" would be to use constraint propagation until the
# implemented strategies fail, then use backtracking. Even so, without
# implementing every possible strategy you can never be sure the puzzle
# will be solvable this way, so backtracking isn't that useful. 

import init_sudoku
import validate_sudoku
import peers_sudoku
import solve_sudoku

def main():
    
    game = init_sudoku.BoardCreation()
    game.initialize()

    valid = validate_sudoku.Validation(game)
    valid.full_validate("provided board")
    game.print_board()

    friends = peers_sudoku.Peers(game)
    friends.assign_peers()
    
    solution = solve_sudoku.Elimination(game, friends)
    solution.solve_board()

    valid.full_validate("solution")
    game.print_board() 


main()