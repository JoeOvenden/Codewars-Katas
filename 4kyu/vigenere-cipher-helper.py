# https://www.codewars.com/kata/52d1bd3694d26f8d6e0000d3/train/python

# The Vigenère cipher is a classic cipher originally developed by Italian cryptographer Giovan Battista Bellaso and published in 1553. It is named after a later French cryptographer Blaise de Vigenère, who had developed a stronger autokey cipher (a cipher that incorporates the message of the text into the key).

# The cipher is easy to understand and implement, but survived three centuries of attempts to break it, earning it the nickname "le chiffre indéchiffrable" or "the indecipherable cipher."

# From Wikipedia:

# The Vigenère cipher is a method of encrypting alphabetic text by using a series of different Caesar ciphers based on the letters of a keyword. It is a simple form of polyalphabetic substitution.

# . . .

# In a Caesar cipher, each letter of the alphabet is shifted along some number of places; for example, in a Caesar cipher of shift 3, A would become D, B would become E, Y would become B and so on. The Vigenère cipher consists of several Caesar ciphers in sequence with different shift values.

# Assume the key is repeated for the length of the text, character by character. Note that some implementations repeat the key over characters only if they are part of the alphabet -- this is not the case here.

# The shift is derived by applying a Caesar shift to a character with the corresponding index of the key in the alphabet.

# Visual representation:

# "my secret code i want to secure"  // message
# "passwordpasswordpasswordpasswor"  // key
# Write a class that, when given a key and an alphabet, can be used to encode and decode from the cipher.

# Example
# var alphabet = 'abcdefghijklmnopqrstuvwxyz';
# var key = 'password';

# // creates a cipher helper with each letter substituted
# // by the corresponding character in the key
# var c = new VigenèreCipher(key, alphabet);

# c.encode('codewars'); // returns 'rovwsoiv'
# c.decode('laxxhsj');  // returns 'waffles'

class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet

    def code(self, text, dir):
        # Since encoding and decoding is just a matter of shifting forward or backwards, this method has the argument dir
        # for direction. Passing in 1 will encode and passing in -1 will decode.
        pw_len = len(self.key)
        new_text = ""
        alphabet_len = len(self.alphabet)
        for i in range(len(text)):
            char = text[i]
            # If char is in alphabet then encode/decode it
            if char in self.alphabet:
                key_letter = self.key[i % pw_len]
                char_current_index = self.alphabet.index(char)
                shift = self.alphabet.index(key_letter)
                new_index = (char_current_index + shift * dir) % alphabet_len
                char = self.alphabet[new_index]
            new_text += char
        return new_text
    
    def encode(self, text):
        return self.code(text, 1)
    
    def decode(self, text):
        return self.code(text, -1)
