# Week 1 Problem 9 - "Pangrams"
# Link - https://www.hackerrank.com/challenges/one-month-preparation-kit-pangrams/

# inputs:
# s = "We promptly judged antique ivory buckles for the next prize"

def pangrams(s):
    s = s.lower()
    alpha = 'abcdefghijklmnopqurstuvwxyz'
    for c in alpha:
        if c not in s:
            return "not pangram"
    return "pangram"

# output = "pangram"