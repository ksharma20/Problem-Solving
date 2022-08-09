# Week 1 Problem 11 - "Subarray Division 1"
# Link - https://www.hackerrank.com/challenges/one-month-preparation-kit-the-birthday-bar/

# inputs:
# s = [2,2,1,3,2]
# d = 4
# m = 2

def birthday(s, d, m):
    count = 0
    n = len(s)
    for i in range(n):
        if sum(s[i:i+m]) == d:
            count += 1
    return count
        
# output = 2