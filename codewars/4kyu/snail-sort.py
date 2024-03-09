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

def next_direction(dir):
    if dir == [1, 0]:
        return [0, 1]
    if dir == [0, 1]:
        return [-1, 0]
    if dir == [-1, 0]:
        return [0, -1]
    if dir == [0, -1]:
        return [1, 0]

def snail(snail_map):
    direction = [1, 0]  # [x, y]
    arr = []
    x = 0, y = 0
    while True:
        pass