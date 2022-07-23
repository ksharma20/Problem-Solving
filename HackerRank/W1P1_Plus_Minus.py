# Week 1 Problem 1 - "Plus Minus"
# Link - https://www.hackerrank.com/challenges/one-month-preparation-kit-plus-minus/

# inputs:
# arr = [-4, 3, -9, 0, 4, 1]

def plusMinus(arr):
    n = len(arr)
    positive = 0
    negetive = 0
    zeroes = 0
    
    for ele in range(n):
        if arr[ele]>0:
            positive += 1
        elif arr[ele]<0:
            negetive += 1
        else:
            zeroes += 1
    
    print("{:.6f}".format(positive/n))
    print("{:.6f}".format(negetive/n))
    print("{:.6f}".format(zeroes/n))


# output = 0.500000 0.333333 0.166667