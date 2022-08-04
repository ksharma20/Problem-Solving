# Week 2 Problem 13 - "SUM vs XOR"
# Link - https://www.hackerrank.com/challenges/one-month-preparation-kit-sum-vs-xor/

# inputs:
# n = 10

def sumXor(n):
    # count = 0
    # for x in range(n+1):
    #     if n^x == n+x:
    #         count += 1
    # return count
    return 1 if n==0 else 2**(bin(n).count('0',2))

# output = 4