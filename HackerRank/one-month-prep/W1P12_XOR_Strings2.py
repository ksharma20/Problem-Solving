# Week 1 Problem 12 - "XOR Strings 2"
# Link - https://www.hackerrank.com/challenges/one-month-preparation-kit-strings-xor/

# inputs:
# s = 10101
# t = 00101

def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            res += '0'
        else:
            res += '1'

    return res

# output = 10000