# Write a method that takes a field for well-known board game "Battleship" as an argument and returns true if it has a valid disposition of ships, false otherwise. Argument is guaranteed to be 10*10 two-dimension array. Elements in the array are numbers, 0 if the cell is free and 1 if occupied by ship.

# Battleship (also Battleships or Sea Battle) is a guessing game for two players. Each player has a 10x10 grid containing several "ships" and objective is to destroy enemy's forces by targetting individual cells on his field. The ship occupies one or more cells in the grid. Size and number of ships may differ from version to version. In this kata we will use Soviet/Russian version of the game.


# Before the game begins, players set up the board and place the ships accordingly to the following rules:
# There must be single battleship (size of 4 cells), 2 cruisers (size 3), 3 destroyers (size 2) and 4 submarines (size 1). Any additional ships are not allowed, as well as missing ships.
# Each ship must be a straight line, except for submarines, which are just single cell.

# The ship cannot overlap or be in contact with any other ship, neither by edge nor by corner.

"""

"""

class Direction:
    # The position of a cell is stored as such: [row_index, col_index] meaning if you want to find next cell in a given 
    # direction, dir, you can do: cell_index[dir] += 1 and then field[cell_index[0]][cell_index[1]] will give you the next cell
    VERTICAL = 0
    HORIZONTAL = 1


def in_field(field, row_index, col_index):
    # Returns True if field[row_index][col_index] is a valid position. (Counting -1 as an invalid index)
    if row_index < 0 or col_index < 0:
        return False
    if row_index >= len(field) or col_index >= len(field[0]):
        return False
    return True


def invalid_diagonals(field, row_index, col_index):
    # Returns True if the diagonally adjacent cells of field[row_index][col_index] are occupied.
    for row_adjustment in [-1, 1]:
        for col_adjustment in [-1, 1]:
            r, c = row_index + row_adjustment, col_index + col_adjustment
            if in_field(field, r, c) and field[r][c] == 1:
                return True
    return False


def find_boat(field, row_index, col_index):
    # Check to see if there is a valid boat at the given cell and if so returns the length of the boat
    # If there the field is invalid, returns -1
    # Also removes the boat from the field, i.e. sets all 1's of the boat to 0

    # Note: In validate_battlefield() the cells are checked from top to bottom and left to right, meaning that
    # the cell that is being checked with always be the lest-most cell for horizontal boats and the upper-most cell for 
    # vertical boats

    """
    IMPROVEMENTS: Re-write code using classes so that there doesn't have to be so much messing around with indexes
    and can simply do cell.next_cell(direction). Incorporating index validation into this would be very nice as well.
    Current code is messy.
    """

    direction = None
    length = 1
    print(f"Boat cell at [{row_index}, {col_index}]. Current length: {length}")

    # Set first boat cell to 0 as we want to remove the boat after finding it.
    field[row_index][col_index] = 0

    # Find orientation of boat (assuming it is a valid placement, validation will come later)
    if in_field(field, row_index + 1, col_index) and field[row_index + 1][col_index] == 1:
        direction = Direction.VERTICAL
        
    elif in_field(field, row_index, col_index + 1) and field[row_index][col_index + 1] == 1:
        direction = Direction.HORIZONTAL

    if invalid_diagonals(field, row_index, col_index):
        return -1

    # No direction -> length 1 boat
    if direction == None:
        print(f"Length 1 boat found.")
        return 1
    
    # Boat is now assumed to have length > 1 and have a given direction
    # Must now find all cells of the boat and check to see if there are any infractions.
    cell_indexes = [row_index, col_index]
    while True:
        cell_indexes[direction] += 1

        if in_field(field, cell_indexes[0], cell_indexes[1]) and field[cell_indexes[0]][cell_indexes[1]] == 1:
            length += 1
            print(f"New boat cell at [{cell_indexes[0]}, {cell_indexes[1]}]. Length: {length}")

            # Set cell to 0 as we want to remove the boat from the board once it has been checked
            field[cell_indexes[0]][cell_indexes[1]] = 0

            # A boat length greater than 4 is invalid
            if length > 4:
                return -1

            # Check diagonals
            if invalid_diagonals(field, cell_indexes[0], cell_indexes[1]):
                return -1

            # For a vertical boat, check to the left and right of a boat cell and if it is occupied then the position is invalid
            # For a horizontal boat, check above and below.
            for i in [-1, 1]:
                check_cell_index = [cell_indexes[0], cell_indexes[1]]
                check_cell_index[direction - 1] += i
                if in_field(field, check_cell_index[0], check_cell_index[1]) and field[check_cell_index[0]][check_cell_index[1]] == -1:
                    return -1

        # In the case that we have reached the end of the boat and found no infractions, then return the boat length.
        # This boats placement is valid.
        else:
            break

    print(f"Boat finished. Length: {length}")
    return length




def check_too_many_boats(boats):
    # Checks to see if there a more boats of a certain type than there should be
    # Returns True if there are two many boats and False otherwise
    boat_amounts_limit = [4, 3, 2, 1]
    for i in range(len(boats)):
        if boats[i] > boat_amounts_limit[i]:
            return True
    return False

    
def check_enough_boats(boats):
    # Checks that the amount of boats is [4, 3, 2, 1]
    return boats == [4, 3, 2, 1]


def validate_battlefield(field):
    boat_counts = [0, 0, 0, 0]      # number of: [length 1 boats, length 2, length 3, length 4]
    for row_index in range(len(field)):
        for col_index in range(len(field[0])):

            # If a cell is occupied, then find the entirety of the boat, record the length, and remove it.
            # If any placement infractions are found, then return False
            if field[row_index][col_index] == 1:
                boat_length = find_boat(field, row_index, col_index)
                print(f"Len: {boat_length} at [{row_index}, {col_index}]")
                if boat_length == -1:
                    return False
                boat_counts[boat_length - 1] += 1
                print(boat_counts)
                if check_too_many_boats(boat_counts):
                    return False

    # After all boats have been found, check that there are the correct number of boats of each type.
    if check_enough_boats(boat_counts) == False:
        return False
    return True