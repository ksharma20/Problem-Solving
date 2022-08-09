# Week 1 Problem 10 - "Permuting 2 Arrays"
# Link - https://www.hackerrank.com/challenges/one-month-preparation-kit-two-arrays/

# inputs:
# A = [0,1]
# B = [0,2]
# k = 1

def twoArrays(k, A, B):
    n = len(A)
    for _ in range(n):
        ma = max(A); mb = min(B)
        if ma + mb >= k:
            A.remove(ma)
            B.remove(mb)
        else:
            return "NO"
    return "YES"

# output = "YES"