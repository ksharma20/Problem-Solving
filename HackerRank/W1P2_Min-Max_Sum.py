# Week 1 Problem 2 - "Min-Max Sum"
# Link - https://www.hackerrank.com/challenges/one-month-preparation-kit-mini-max-sum/

# inputs
# arr = [1, 2, 3, 4, 5]

def miniMaxSum(arr):
    mini = arr.copy()
    mini.remove(max(mini))
    maxi = arr.copy()
    maxi.remove(min(maxi))
    
    print(sum(mini), sum(maxi))

# output = 10 14