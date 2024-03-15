# Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:

#   12 ==> 21
#  513 ==> 531
# 2017 ==> 2071
# If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift, None in Rust):

#   9 ==> -1
# 111 ==> -1
# 531 ==> -1

from itertools import permutations

def next_bigger(n):
    """
    Method: 
    Start with the second to last digit and see if swapping it with the last
    digit would make a bigger number.
    If not, move onto the third to last number and check if swapping with the last number
    would make a bigger number. If not check if swapping with the second to last.
    If not, move onto the ...
    If not, onto the first number and check swapping with the last number, ... the second
    to last, ... , the third to last , ....... , the second number.
    
    If a swap can be made to make a larger number, everything to the right of the bigger
    digit that was swapped should be sorted from smallest to largest going left to right.
    
    Example: 5999643320
    The only swap that can be made is the 6 with the 5. 
    This gives 6999543320. This however isn't the next bigger number, so we must sort
    all the digits to the right of the 6 to give 6023345999
    """
    n = list(str(n))
    # Try to swap left and right hand digits in the number starting with those that
    # represent the least value. I.e. starting from the right
    for left_index in range(len(n) - 2, -1, -1):
        for right_index in range(len(n) -1, left_index, -1):
            digit_left = int(n[left_index])
            digit_right = int(n[right_index])
            # If the left digit being compared is less than the rigth then 
            # swap the two digits and then sort everything to the right of the left index
            if digit_left < digit_right:
                n[left_index], n[right_index] = n[right_index], n[left_index]
                lhs = n[:left_index + 1]
                rhs = n[left_index + 1:]
                rhs.sort()
                n = lhs + rhs
                return int("".join(n))
    return -1