# Week 1 Problem 7 - "Diagonal Difference"
# Link - https://www.hackerrank.com/challenges/one-month-preparation-kit-diagonal-difference/

# inputs:
# n = 3
# arr = [
#     [11, 2, 4],
#     [4, 5, 6],
#     [10, 8, -12]]

def diagonalDifference(arr, n):
    # print(n)
    # print(arr)
    left = 0
    right = 0
    for i in range(n):
        left += arr[i][i]
        right += arr[i][n-i-1]
        # print(left, end="\t")
        # print(right)
        
    return abs(left-right)

# output = 15