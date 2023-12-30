import numpy as np

# This class is a relic of the backtracking version.

# It compares, in each unit (row, column and 3x3 square), every member to
# the provided member.

# With backtracking, I had to check for validity every time I added a member,
# so it seemed like a sensible organisation. 
# With constraint propagation, I don't need to check for validity because
# a new member is added only when it's the only possible choice. We'll
# have an invalid member only if the code is wrong.

# It's not very efficient when used to validate a full board, because
# we have to loop through every cell in a unit until we find a duplicate of
# our input cell, to validate that unit. Meaning, we loop 9 times per unit
# to validate a full board.

# We could instead pass once over each row, each column and each square
# and put the result in a dictionary or list, then check for duplicates.


# In these methods, we regularly have to check for cell != 0 because
# the baseline member of my board is zero. 

class Validation():
    def __init__(self, game):
        self.game = game
        self.dic_square = {0 : [0, 1, 2], 3 : [3,4,5], 6 : [6,7,8]}
    
    def full_validate(self, strg):
        for row_index in range(0,9):
            for column_index in range(0,9):
                if not (self.row_validate(row_index, column_index) and
                self.column_validate(row_index, column_index) and
                self.square_validate(row_index, column_index)):
                    print("Unfortunately, there are duplicates:")
                    self.game.print_board()
                    exit()
        print(f"\nThe {strg} is valid:")

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
    
    # Couldn't think of a mathematical way to efficiently navigate 3x3 squares
    # then, so I wrote a dictionary that determines what rows and cols we are
    # in based on input coordinates.
    # The method in "calculate_peers()" is somewhat more elegant.

    def square_validate(self, x, y):
        for key in self.dic_square:
            if x in self.dic_square[key]:
                row_range = self.dic_square[key]
            if y in self.dic_square[key]:
                column_range = self.dic_square[key]

        counter = 0
        for row in self.game.board[row_range]:
            for cell in row[column_range]:
                if cell == self.game.board[x][y] and cell != 0:
                    counter += 1
                    if counter > 1:
                        return False
        return True
