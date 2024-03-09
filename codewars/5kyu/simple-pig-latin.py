# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

def pig_it(text):
    words = text.split(" ")
    for i in range(len(words)):
        if words[i] in ["?", "!"]:
            continue
        words[i] = words[i][1:] + words[i][0] + "ay"
    return " ".join(words)