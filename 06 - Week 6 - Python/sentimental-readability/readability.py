from cs50 import get_string
import re

# ask user for some text
text = get_string("Text: ")

# count letters (a-z, A-Z only)
letters = sum(1 for c in text if c.isalpha())

# count words (split by spaces)
words = len(text.split())

# count sentences (. ! ?)
sentences = sum(1 for c in text if c in ".!?")

# Coleman-Liau formula (sounds scarier than it is lol)
L = letters / words * 100
S = sentences / words * 100
index = round(0.0588 * L - 0.296 * S - 15.8)

# now decide what to print
if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print(f"Grade {index}")
