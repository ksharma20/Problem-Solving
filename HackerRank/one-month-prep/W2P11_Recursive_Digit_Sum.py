# Week 2 Problem 11 - "Recursive Digit Sum"
# Link - https://www.hackerrank.com/challenges/one-month-preparation-kit-recursive-digit-sum/

# inputs:
# n = "9875"
# k = 4

def superDigit(n, k):
    if len(n) == 1 and k == 1:
        return n
    p = list(map(int,n))
    sp = str(sum(p)*k)
    return superDigit(sp, 1)

# output = 8