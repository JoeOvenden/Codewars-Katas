# Snail Sort
# Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
# For better understanding, please follow the numbers of the next array consecutively:

# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]

# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python

def next_direction(direction):
    if direction == [1, 0]:
        return [0, 1]
    if direction == [0, 1]:
        return [-1, 0]
    if direction == [-1, 0]:
        return [0, -1]
    if direction == [0, -1]:
        return [1, 0]


def move(pos, direction, multiplier=1):
    for i in range(2):
        pos[i] += direction[i] * multiplier


def pos_out_of_bounds(snail_map, pos):
    if pos[0] < 0 or pos[0] >= len(snail_map) or pos[1] < 0 or pos[1] >= len(snail_map[0]):
        return True


def snail(snail_map):
    direction = [0, 1]
    arr = []
    pos = [0, 0]
    remaining = len(snail_map) * len(snail_map[0])
    while remaining > 0:
        if pos_out_of_bounds(snail_map, pos) or snail_map[pos[0]][pos[1]] == None:
            move(pos, direction, multiplier=-1)
            direction = next_direction(direction)
            move(pos, direction)
            continue
        arr.append(snail_map[pos[0]][pos[1]])
        snail_map[pos[0]][pos[1]] = None
        remaining -= 1
        move(pos, direction)
    return arr

if __name__ == "__main__":
    arr = [[1, 2, 3],
           [8, 9, 4],
           [7, 6, 5]]
    print(snail(arr))