# This class is a relic of the backtracking version.

# It compares, in each unit (row, column or 3x3 square), every member to
# the provided member.

# With backtracking, I had to check for validity every time I added a member,
# so this seemed like a sensible organisation. 
# With constraint propagation, I don't need to check for validity because
# a new member is added only when it's the only possible choice. We
# have an invalid member only if the code is faulty.

# It's inefficient when used to validate a full board, because
# we have to loop 9 times through a unit to ensure there are no duplicates.
# We could instead iterate once over each row, each column and each square
# and put the result in a dictionary or list, then check for duplicates.

import numpy as np


class Validation():
    def __init__(self, game):
        self.game = game
    
    def full_validate(self, strg):
        for row_index in range(0,9):
            for column_index in range(0,9):
                if not (self.row_validate(row_index, column_index) and
                self.column_validate(row_index, column_index) and
                self.square_validate(row_index, column_index)):
                    print("Unfortunately, there are duplicates:")
                    self.game.print_board()
                    exit()
        print(f"\n\nThe {strg} is valid:\n")

    def row_validate(self, x, y):
        for index, cell in enumerate(np.nditer(self.game.board[x:x+1, :])):
            if cell == self.game.board[x][y] and cell != 0 and index != y:         
                return False
        return True
    
    def column_validate(self, x, y):
         for index, cell in enumerate(np.nditer(self.game.board[:, y:y+1])):
            if cell == self.game.board[x][y] and cell != 0 and index != x:         
                return False
         return True
    
    # Couldn't think of an efficient way to navigate 3x3 squares
    # then, so I wrote a dictionary that determines what rows and cols we are
    # in based on input coordinates.
    # The calculate_peers method uses a different strategy.
    def square_validate(self, x, y):
        coordinate_to_square_unit = {0 : [0, 1, 2], 3 : [3,4,5], 6 : [6,7,8]}
        for key in coordinate_to_square_unit:
            if x in coordinate_to_square_unit[key]:
                row_range = coordinate_to_square_unit[key]
            if y in coordinate_to_square_unit[key]:
                column_range = coordinate_to_square_unit[key]

        counter = 0
        for row in self.game.board[row_range]:
            for cell in row[column_range]:
                if cell == self.game.board[x][y] and cell != 0:
                    counter += 1
                    if counter > 1:
                        return False
        return True