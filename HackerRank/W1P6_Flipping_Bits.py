# Week 1 Problem 6 - "Flipping Bits"
# Link - https://www.hackerrank.com/challenges/one-month-preparation-kit-flipping-bits/

# inputs:
# n = 2147483647

def flippingBits(n):
    # print(n)
    n = list(bin(n)[2:].zfill(32)) 
    # print(n)
    for i in range(32):
        if n[i] == str(0):
            n[i] = str(1)
        else:
            n[i] = str(0)
    # print(n)
    return int("".join(n),2)

# output = 2147483648