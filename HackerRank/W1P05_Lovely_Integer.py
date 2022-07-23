# Week 1 Problem 5 - "Lovely Integer"
# Link - https://www.hackerrank.com/challenges/one-month-preparation-kit-lonely-integer/

# inputs:
# a = [1,2,3,4,3,2,1]

def lonelyinteger(a):
    n = len(a)
    lonely = None
    for i in range(n):
        if a.count(a[i]) == 1:
            lonely = a[i]
            break
    return lonely if lonely else "No Element"

# output = 4