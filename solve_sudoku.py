# In our "possibles" dictionary we assigned every cell the possibles 1-9.
# However, we need two tools:
#   1. once a value is assigned to a cell, we need to remove that
#      value from its peers' possibles (eliminate_possibles)
#   2. we need to remove that cell from the possibles dictionary, as
#      it is considered "solved" (eliminate_from_possibles_dic). 
#      Remember, with constraint propagation you only make mistakes if your 
#      code is faulty; you never revise a cell assignment.

# We then implement two Sudoku strategies:
#   1. Naked single: we check every coordinate in our dictionary of possibles;
#      if any of them has only one possible, we assign that value. Simple
#      puzzles can often be solved with this alone.
#   2. Hidden single: we check every unit (each row, column and 3x3 square)
#      in our dictionary of possibles. If only one of the unit's members has 
#      a given possible, we assign that value.
#      
#      For this, we make a list of all the possibles of a unit and use
#      bincount to determine if there's a specific value (given by the
#      bincount array position) that appears only once.
#
#      If so, we iterate through our unit's coordinates and assign the 
#      value if it's part of the coordinates' possibles. Not very pretty.

import numpy as np


class Elimination():
    def __init__(self, game, peers):
        self.game = game
        self.peers = peers

    def solve_board(self):
        while len(self.peers.possibles_dictionary) > 0:
            self.eliminate_possibles()
            self.eliminate_from_possibles_dic()
            self.naked_single()
            self.hidden_single_row_col('row')
            self.hidden_single_row_col('col')
            self.hidden_single_square()

    def eliminate_possibles(self):
        for index, digit in np.ndenumerate(self.game.board):
            if digit > 0:
                for peer in self.peers.peers_dictionary[index]:
                    if peer in self.peers.possibles_dictionary and digit in self.peers.possibles_dictionary[peer]:
                            self.peers.possibles_dictionary[peer].remove(digit)

    def eliminate_from_possibles_dic(self):
        for index, digit in np.ndenumerate(self.game.board):
            if digit > 0 and index in self.peers.possibles_dictionary:
                del self.peers.possibles_dictionary[index]

    def naked_single(self):
        for key in self.peers.possibles_dictionary:
            # if len == 1, it means a coordinate has only 1 possible
            if len(self.peers.possibles_dictionary[key]) == 1:
                digit = self.peers.possibles_dictionary[key]
                self.game.board[key] = digit[0]

    def hidden_single_row_col(self, axis):
        for axis_index in range(9):
            possibles_list = []
            for coordinates in self.peers.possibles_dictionary:
                if coordinates[0 if axis == 'row' else 1] == axis_index:
                    possibles_list.extend(self.peers.possibles_dictionary[coordinates])

            bin_list = np.bincount(possibles_list)
            for index, count in enumerate(bin_list):
                if count == 1:
                    for coordinates in self.peers.possibles_dictionary:
                        if coordinates[0 if axis == 'row' else 1] == axis_index and index in self.peers.possibles_dictionary[coordinates]:
                            self.game.board[coordinates] = index

    def hidden_single_square(self):
        for row_index in range(3, 10, 3):
            for col_index in range(3, 10, 3):
                min_index = (row_index - 3, col_index - 3)
                max_index = (row_index, col_index)
                
                possibles_list = []
                for coordinates in self.peers.possibles_dictionary:
                    if min_index[0] <= coordinates[0] < max_index[0] and min_index[1] <= coordinates[1] < max_index[1]:
                        possibles_list.extend(self.peers.possibles_dictionary[coordinates])

                bin_list = np.bincount(possibles_list)
                for index, count in enumerate(bin_list):
                    if count == 1:
                        for coordinates in self.peers.possibles_dictionary:
                            if min_index[0] <= coordinates[0] < max_index[0] and min_index[1] <= coordinates[1] < max_index[1] and index in self.peers.possibles_dictionary[coordinates]:
                                self.game.board[coordinates] = index