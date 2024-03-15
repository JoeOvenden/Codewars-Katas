# DESCRIPTION:
# Write a function that will solve a 9x9 Sudoku puzzle. The function will take one argument consisting of the 2D puzzle array, with the value 0 representing an unknown square.

# The Sudokus tested against your function will be "easy" (i.e. determinable; there will be no need to assume and test possibilities on unknowns) and can be solved with a brute-force approach.

# For Sudoku rules, see the Wikipedia article.

# puzzle = [[5,3,0,0,7,0,0,0,0],
#           [6,0,0,1,9,5,0,0,0],
#           [0,9,8,0,0,0,0,6,0],
#           [8,0,0,0,6,0,0,0,3],
#           [4,0,0,8,0,3,0,0,1],
#           [7,0,0,0,2,0,0,0,6],
#           [0,6,0,0,0,0,2,8,0],
#           [0,0,0,4,1,9,0,0,5],
#           [0,0,0,0,8,0,0,7,9]]

# sudoku(puzzle)
# # Should return
#  [[5,3,4,6,7,8,9,1,2],
#   [6,7,2,1,9,5,3,4,8],
#   [1,9,8,3,4,2,5,6,7],
#   [8,5,9,7,6,1,4,2,3],
#   [4,2,6,8,5,3,7,9,1],
#   [7,1,3,9,2,4,8,5,6],
#   [9,6,1,5,3,7,2,8,4],
#   [2,8,7,4,1,9,6,3,5],
#   [3,4,5,2,8,6,1,7,9]]

from itertools import product 

class Problem:
    def __init__(self, puzzle):
        self.puzzle = puzzle


    def display(self):
        print("--" * 10)
        for row in self.puzzle:
            print('|', end="")
            for cell in row:
                print(f"{str(cell)}|", end="")
            print()
        print("--" * 10)


    def get_square(self, row, column):
        # For a given cell return the set of numbers that are in it's 3x3 square. Row and column are indices

        # Get the lowest index for row and column in the 3x3 square
        row -= row % 3
        column -= column % 3

        square_cell_indexes = product([row + i for i in range(3)], [column + i for i in range(3)])
        numbers = set([self.puzzle[i][j] for (i, j) in square_cell_indexes]) - set([0])
        return numbers


    def get_row(self, row):
        # For a given row index, returns the set of numbers in that row
        return set(self.puzzle[row]) - set([0])

    
    def get_column(self, column):
        # For a given column index, returns the set of numbers in that column
        return set([self.puzzle[row][column] for row in range(9)]) - set([0])


    def analyse_cells(self):
        # Looks at each cell on the board and checks to see if a number can be filled in
        for row in range(9):
            for column in range(9):
                if self.puzzle[row][column] == 0:
                    # Start with the set of numbers from 1 to 9 and then subtract all the numbers in that row, column and square
                    possible_numbers = set(range(1, 10))
                    possible_numbers -= self.get_row(row)
                    possible_numbers -= self.get_column(column)
                    possible_numbers -= self.get_square(row, column)
                    # If there is only 1 possible number then we fill it in
                    if len(possible_numbers) == 1:
                        self.puzzle[row][column] = possible_numbers.pop()


    def is_solved(self):
        for row in self.puzzle:
            if 0 in row:
                return False
        return True


    def solve(self):
        while not self.is_solved():
            self.analyse_cells()
        return self.puzzle


def sudoku(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""
    P = Problem(puzzle)
    return P.solve()


if __name__ == "__main__":
    puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]
    sudoku(puzzle)