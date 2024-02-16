# In Sudoku, constraint propagation makes use of "possibles" and "peers" to
# solve puzzles. 
# Possibles are all the values that are possible for a member (cell) to adopt
# for a given board state. Peers are every member in the same row, column and
# 3x3 square; every member has 20 peers.

# Peers are used to propagate possibles. Every time we assign a 
# value to a member, we go through its peers and remove that value from
# their list of possibles.

# I make use of two dictionaries for this, where each board coordinate is a
# key and its value is 1. a list of possibles and; 2. a list of peers
# respectively.

import numpy as np


class Peers():
    def __init__(self, game):
        self.game = game

        self.possibles_dictionary = {(x, y): list(range(1, 10)) for x in range(0, 9) for y in range(0, 9)}
        self.peers_dictionary = {(x, y): [] for x in range(0, 9) for y in range(0, 9)}

    def assign_peers(self):
        for row_index, row in enumerate(self.game.board):
            for col_index, _ in enumerate(row):
                self.calculate_peers(row_index, col_index)

    def calculate_peers(self, x, y):
        for col_index in range(0, 9):
            self.peers_dictionary[x, y].append((x, col_index))
        for row_index in range(0, 9):
            self.peers_dictionary[x, y].append((row_index, y))

        subgrid_x = x // 3
        subgrid_y = y // 3
        
        for row_index in range(subgrid_x * 3, (subgrid_x + 1) * 3):
            for col_index in range(subgrid_y * 3, (subgrid_y + 1) * 3):
                self.peers_dictionary[x, y].append((row_index, col_index))

                    
