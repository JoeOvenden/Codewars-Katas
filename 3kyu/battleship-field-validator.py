# Write a method that takes a field for well-known board game "Battleship" as an argument and returns true if it has a valid disposition of ships, false otherwise. Argument is guaranteed to be 10*10 two-dimension array. Elements in the array are numbers, 0 if the cell is free and 1 if occupied by ship.

# Battleship (also Battleships or Sea Battle) is a guessing game for two players. Each player has a 10x10 grid containing several "ships" and objective is to destroy enemy's forces by targetting individual cells on his field. The ship occupies one or more cells in the grid. Size and number of ships may differ from version to version. In this kata we will use Soviet/Russian version of the game.


# Before the game begins, players set up the board and place the ships accordingly to the following rules:
# There must be single battleship (size of 4 cells), 2 cruisers (size 3), 3 destroyers (size 2) and 4 submarines (size 1). Any additional ships are not allowed, as well as missing ships.
# Each ship must be a straight line, except for submarines, which are just single cell.

# The ship cannot overlap or be in contact with any other ship, neither by edge nor by corner.

class Direction:
    # The position of a cell is stored as such: [row_index, col_index] meaning if you want to find next cell in a given 
    # direction, dir, you can do: cell_index[dir] += 1 and then field[cell_index[0]][cell_index[1]] will give you the next cell
    VERTICAL = 0
    HORIZONTAL = 1


class Problem:
    def __init__(self, field):
        self. field = field
        self.row_count = len(field)
        self.col_count = len(field[0])


    def pos_in_field(self, pos):
        # Returns True if the position is in the field and False otherwise
        if pos[0] < 0 or pos[0] >= self.row_count or pos[1] < 0 or pos[1] >= self.col_count:
            return False
        return True


    def cell_is_occupied(self, pos):
        # Returns True if pos in inside the field and is occupied and False otherwise
        if self.pos_in_field(pos) and self.field[pos[0]][pos[1]] == 1:
            return True
        return False

    
    def invalid_diagonals(self, pos):
        # Returns True if the diagonals to the cell at the given position are occupied and False otherwise
        for row_adjustment in [-1, 1]:
            for col_adjustment in [-1, 1]:
                row, col = pos[0] + row_adjustment, pos[1] + col_adjustment
                diagonal = [row, col]
                if self.cell_is_occupied(diagonal):
                    return True
        return False


    def clear_cell(self, pos):
        self.field[pos[0]][pos[1]] = 0


    def get_next_pos(self, pos, direction, distance=1):
        # Returns the position of the next cell over from pos in a given direction. Always in the positive direction
        cell = [pos[0], pos[1]]
        cell[direction] += distance
        return cell


    def orthogonal_cell_is_occupied(self, pos, direction, distance=1):
        # Checks to see if the cell a certain distance away from pos in the given direction is 
        # a) inside the field and b) occupied. If so returns True, otherwise False

        # Note: the distance is always added, i.e. it always goes in the positive direction for the reason explained in
        # the notes of self.find_boat()
        return self.cell_is_occupied(self.get_next_pos(pos, direction, distance))


    def invalid_adjacent_cells(self, pos, direction):
        # For a given direction, checks if the adjacent cells in the opposite direction are occupied
        # Returns True if they are and False otherwise

        # Changing pos[direction - 1] gives a cell in the opposite direction to the given one
        for i in [-1, 1]:
            adjacent_cell = [pos[0], pos[1]]
            adjacent_cell[direction - 1] += i
            if self.cell_is_occupied(adjacent_cell):
                return -1
    

    def find_boat(self, pos):
        # Check to see if there is a valid boat at the given cell and if so returns the length of the boat
        # If there the field is invalid, returns -1
        # Also removes the boat from the field, i.e. sets all 1's of the boat to 0

        # Note: In validate_battlefield() the cells are checked from top to bottom and left to right, meaning that
        # the cell that is being checked with always be the lest-most cell for horizontal boats and the upper-most cell for 
        # vertical boats

        direction = None
        length = 0

        # Find orientation of boat (assuming it is a valid placement, validation will come later)
        if self.orthogonal_cell_is_occupied(pos, Direction.VERTICAL):
            direction = Direction.VERTICAL
        elif self.orthogonal_cell_is_occupied(pos, Direction.HORIZONTAL):
            direction = Direction.HORIZONTAL

        # No direction -> length 1 boat
        if direction == None:
            return 1
        
        cell = [pos[0], pos[1]]
        # Boat is now assumed to have length > 1 and have a given direction
        # Must now find all cells of the boat and check to see if there are any infractions.

        while True:
            # If found adjacent boat cell
            if self.cell_is_occupied(cell):
                length += 1

                # Set cell to 0 as we want to remove the boat from the board once it has been checked
                self.clear_cell(cell)

                # A boat length greater than 4 is invalid
                if length > 4:
                    return -1

                # Check diagonals
                if self.invalid_diagonals(cell):
                    return -1

                # For a vertical boat, check to the left and right of a boat cell and if it is occupied then the position is invalid
                # For a horizontal boat, check above and below.
                if self.invalid_adjacent_cells(cell, direction):
                    return -1

            # In the case that we have reached the end of the boat and found no infractions, then return the boat length.
            else:
                break

            cell = self.get_next_pos(cell, direction)

        return length

    
    def check_too_many_boats(self, boats):
        # Checks to see if there a more boats of a certain type than there should be
        # Returns True if there are two many boats and False otherwise
        boat_amounts_limit = [4, 3, 2, 1]
        for i in range(len(boats)):
            if boats[i] > boat_amounts_limit[i]:
                return True
        return False

        
    def check_enough_boats(self, boats):
        # Checks that the amount of boats is [4, 3, 2, 1]
        return boats == [4, 3, 2, 1]


    def is_valid(self):
        boat_counts = [0, 0, 0, 0]      # number of: [length 1 boats, length 2, length 3, length 4]
        for row_index in range(self.row_count):
            for col_index in range(self.col_count):
                pos = [row_index, col_index]

                # If a cell is occupied, then find the entirety of the boat, record the length, and remove it.
                # If any placement infractions are found, then return False
                if self.cell_is_occupied(pos):
                    boat_length = self.find_boat(pos)
                    if boat_length == -1:
                        return False

                    boat_counts[boat_length - 1] += 1
                    if self.check_too_many_boats(boat_counts):
                        return False

        # After all boats have been found, check that there are the correct number of boats of each type.
        if self.check_enough_boats(boat_counts) == False:
            return False
        return True




def validate_battlefield(field):
    P = Problem(field)
    return P.is_valid()