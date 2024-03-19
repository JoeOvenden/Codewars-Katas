# https://www.codewars.com/kata/esolang-interpreters-number-3-custom-paintf-star-star-k-interpreter

# The Task
# Your task is to implement a custom Paintfuck interpreter interpreter()/Interpret which accepts the following arguments in the specified order:

# code - Required. The Paintfuck code to be executed, passed in as a string. May contain comments (non-command characters), in which case your interpreter should simply ignore them. If empty, simply return the initial state of the data grid.
# iterations - Required. A non-negative integer specifying the number of iterations to be performed before the final state of the data grid is returned. See notes for definition of 1 iteration. If equal to zero, simply return the initial state of the data grid.
# width - Required. The width of the data grid in terms of the number of data cells in each row, passed in as a positive integer.
# height - Required. The height of the data grid in cells (i.e. number of rows) passed in as a positive integer.
# A few things to note:

# Your interpreter should treat all command characters as case-sensitive so N, E, S and W are not valid command characters
# Your interpreter should initialize all cells within the data grid to a value of 0 regardless of the width and height of the grid
# In this implementation, your pointer must always start at the top-left hand corner of the data grid (i.e. first row, first column). This is important as some implementations have the data pointer starting at the middle of the grid.
# One iteration is defined as one step in the program, i.e. the number of command characters evaluated. For example, given a program nessewnnnewwwsswse and an iteration count of 5, your interpreter should evaluate nesse before returning the final state of the data grid. Non-command characters should not count towards the number of iterations.
# Regarding iterations, the act of skipping to the matching ] when a [ is encountered (or vice versa) is considered to be one iteration regardless of the number of command characters in between. The next iteration then commences at the command right after the matching ] (or [).
# Your interpreter should terminate normally and return the final state of the 2D data grid whenever any of the mentioned conditions become true: (1) All commands have been considered left to right, or (2) Your interpreter has already performed the number of iterations specified in the second argument.
# The return value of your interpreter should be a representation of the final state of the 2D data grid where each row is separated from the next by a CRLF (\r\n). For example, if the final state of your datagrid is
# [
#   [1, 0, 0],
#   [0, 1, 0],
#   [0, 0, 1]
# ]
# ... then your return string should be "100\r\n010\r\n001".

import re

class Problem:
    def __init__(self, code, iterations, width, height):
        self.code = re.sub('[^nesw*\[\]]', '', code)
        self.iterations = iterations
        self.width = width
        self.height = height
        self.setup_grid()
            
    
    def setup_grid(self):
        self.grid = []
        for i in range(self.height):
            row = [0] * self.width
            self.grid.append(row)


    def move(self, direction):
        if direction == "n":
            self.row_pointer -= 1
        elif direction == "s":
            self.row_pointer += 1
        elif direction == "e":
            self.col_pointer += 1
        elif direction == "w":
            self.col_pointer -= 1
        self.row_pointer %= self.height
        self.col_pointer %= self.width


    def flip_bit(self):
        print(self.grid[self.row_pointer])
        self.grid[self.row_pointer][self.col_pointer] = int(not self.grid[self.row_pointer][self.col_pointer])

    def jump(self, direction):
        # direction = 1 -> jumping forwards, direction = -1 -> jumping backwards
        counter = 1
        while counter != 0:
            self.code_pointer += direction
            char = self.code[self.code_pointer]
            if char == "[":
                counter += direction
            elif char == "]":
                counter -= direction


    def jump_forward(self):
        self.jump(1)


    def jump_back(self):
        self.jump(-1)


    def current_bit(self):
        return self.grid[self.row_pointer][self.col_pointer]


    def get_return_string(self):
        string = ""
        for i in range(self.height):
            string += "".join([str(digit) for digit in self.grid[i]])
            if i != self.height - 1:
                string += "\r\n"
        return string


    def solve(self):
        self.iterations_passed = 0
        self.row_pointer = 0
        self.col_pointer = 0
        self.code_pointer = 0
        self.code_length = len(self.code)
        while self.code_pointer < self.code_length and self.iterations_passed < self.iterations:
            char = self.code[self.code_pointer]
            if char in ["n", "e", "s", "w"]:
                self.move(char)
            elif char == "*":
                self.flip_bit()
            elif char == "[" and self.current_bit() == 0:
                self.jump_forward()
            elif char == "]" and self.current_bit() != 0:
                self.jump_back()
            self.code_pointer += 1
            self.iterations_passed += 1
        return self.get_return_string()


def interpreter(code, iterations, width, height):
    P = Problem(code, iterations, width, height)
    return P.solve()