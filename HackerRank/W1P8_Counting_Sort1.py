# Week 1 Problem 8 - "Counting Sort 1"
# Link - https://www.hackerrank.com/challenges/one-month-preparation-kit-countingsort1/

# inputs:
# arr = [1,1,3,2,1]

def countingSort(arr):
    result = [0 for _ in range(100)]
    for i in arr:
        result[i] += 1
        
    # sortedarr = []
    # for i,e in enumerate(result):
    #     if e > 0:
    #         for j in range(e):
    #             sortedarr.append(i)
    return result

# output = [0,3,1,1]