# Complete the solution so that the function will break up camel casing, using a space between words.

# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""

def solution(s):
    i = 0
    # Move along the string checking if character is upper case
    # If yes, insert space. End loop when you get to the end of the string
    while True:
        try:
            char = s[i]
        except IndexError:
            break
        if char.isupper():
            s = s[:i] + " " + s[i:]
            i += 1
        i += 1
    return s