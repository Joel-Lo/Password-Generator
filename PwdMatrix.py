import random
import time

alphabet = """ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-=_+{}[]:<~`>?;,"'.\\/"""
upperLetters = """ABCDEFGHIJKLMNOPQRSTUVWXYZ"""
lowerLetters = """abcdefghijklmnopqrstuvwxyz"""
numbers = """0123456789"""
symbols = """!@#$%^&*()-=_+{}[]:<~`>?;,"'.\\/"""
letters = upperLetters + lowerLetters

while True:
    while True:
        length = 12 # Number of character combinations
        first_char = random.choice(letters)
        remaining_chars = random.choices(alphabet, k=length - 1)
        word = first_char + "".join(remaining_chars)
        if len(set(word)) == 1:
            continue
        has_upper_letter = any(char in upperLetters for char in word)
        has_lower_letter = any(char in lowerLetters for char in word)
        has_number = any(char in numbers for char in word)
        has_symbol = any(char in symbols for char in word)
        if has_upper_letter and has_lower_letter and has_number and has_symbol:
            break
    print(word)
    time.sleep(0.01)  # 1000ms = 1s