# Week 2 Problem 6 - "Max Min"
# Link - https://www.hackerrank.com/challenges/one-month-preparation-kit-angry-children/

# inputs:
# k = 2
# arr = [1,4,7,2]

def maxMin(k, arr):
    arr = sorted(arr)
    n = len(arr)
    ufness = arr[-1]
    for i in range(n-k+1):
        ufness = min(arr[i+k-1]-arr[i], ufness)
    
    return ufness

# output = 1