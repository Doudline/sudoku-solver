import numpy as np

class BoardCreation():
    def __init__(self):
        self.board = np.zeros((9,9), dtype=np.int64)
        self.user_input = ""

    def initialize(self):
        valid_input = 0
        while valid_input == 0:
            self.user_input = input("Please provide a valid 9x9 Sudoku grid. There must be at least 17 hints.\nHints must between 1 and 9 inclusive, and empty cases must be represented by '0', '-' or '.'.\n>: ")
    
            valid_input = self.check_input()
        self.create_board()

    def check_input(self):
        cells_counter = 0
        hints_counter = 0

        for value in self.user_input:    
            if '0' <= value <= '9' or value == '-' or value == '.':
                cells_counter += 1
                if '0' < value <= '9':
                    hints_counter += 1

        print(f"\nThank you. There are {cells_counter} cells and {hints_counter} hints.\n")
        if cells_counter != 81 or hints_counter < 17:
            return 0
        return 1
          
    def create_board(self):
        row, column = 0, 0
        
        for value in self.user_input:    
            if value.isnumeric() or value == '-' or value == '.':
                if value.isnumeric():
                    self.board[row][column] = value
                column += 1
                if column >= self.board.shape[1]:
                    column = 0
                    row += 1    

    def print_board(self):
        for i, row in enumerate(self.board):
            for j, cell in enumerate(row):
                print(f"{cell} ", end='')
                if j == 2 or j == 5:
                    print("| ", end='')
            print()
            if i == 2 or i == 5:
                print("-" * 22)