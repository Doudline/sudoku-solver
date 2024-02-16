# My initial solution used backtracking, which solved many puzzles
# almost instantly even with relatively few clues.
# However, puzzles with few clues, clues that were stacked at the end,
# or with certain digit orders (e.g 9-8-7-6-5-4-3-2-1 on the first row) took
# too long.

# Instead, I rewrote the program using constraint propagation. I implemented
# only two strategies (naked and hidden singles) therefore it cannot solve
# every puzzle, but relatively simple ones do just fine.

# A simple improvement would be to use constraint propagation until the
# implemented strategies fail, then use backtracking.

import init_sudoku
import validate_sudoku
import peers_sudoku
import solve_sudoku


def main():
    game = init_sudoku.BoardCreation()
    game.initialize_board()

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