# Week 2 Problem 10 - "Sherlock and Array"
# Link - https://www.hackerrank.com/challenges/one-month-preparation-kit-sherlock-and-array/

# inputs:
# arr = [5,6,8,11]

def balancedSums(arr):
    la = len(arr)
    if la < 2:
        return "YES"
    elif la == 2 and arr[0] == arr[1]:
        return "YES"
    else:
        after = sum(arr)-arr[0]
        before = 0
        for i in range(la-1):
            if before == after:
                return "YES"
            else:
                before += arr[i]
                after -= arr[i+1]
                
    return "NO"

# output = "YES"