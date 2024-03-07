# Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

# The binary number returned should be a string.

def add_binary(a,b):
    # Add the numbers together, convert to binary and strip the leading "0b"
    return bin(a + b).lstrip("0b")