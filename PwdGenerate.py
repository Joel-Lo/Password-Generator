import random

length = 12 # Number of character combinations

def gspwd(length):
    alphabet = """ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-=_+{}[]:<~`>?;,"'.\\/"""
    upperLetters = """ABCDEFGHIJKLMNOPQRSTUVWXYZ"""
    lowerLetters = """abcdefghijklmnopqrstuvwxyz"""
    numbers = """0123456789"""
    symbols = """!@#$%^&*()-=_+{}[]:<~`>?;,"'.\\/"""

    while True:
        combo = random.choices(alphabet, k=length)
        word = "".join(combo)
        if len(set(word)) == 1:
            continue
        has_upper_letter = any(char in upperLetters for char in word)
        has_lower_letter = any(char in lowerLetters for char in word)
        has_number = any(char in numbers for char in word)
        has_symbol = any(char in symbols for char in word)
        if has_upper_letter and has_lower_letter and has_number and has_symbol:
            return word
password = gspwd(length)
print(password)
