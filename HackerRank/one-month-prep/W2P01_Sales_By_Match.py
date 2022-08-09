# Week 2 Problem 1 - "Sales By Match"
# Link - https://www.hackerrank.com/challenges/one-month-preparation-kit-sock-merchant/

# inputs:
# n = 7
# arr = [1,2,1,2,1,3,2]

def sockMerchant(n, ar):
    pairs = 0
    pair = []
    for i in ar:
        if i in pair:
            pairs += 1
            pair.remove(i)
        else:
            pair.append(i)
    return pairs
 

# output = 2