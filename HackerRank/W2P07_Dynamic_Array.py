# Week 2 Problem 7 - "Dynamic Array"
# Link - https://www.hackerrank.com/challenges/one-month-preparation-kit-dynamic-array/

# inputs:
# n = 2
# queries = [[1,0,5],[1,1,7],[1,0,3],[2,1,0],[2,1,1]]

def dynamicArray(n, queries):
    result = []
    arr = [ [] for _ in range(n) ]
    lastAnswer = 0
    for e in queries:
        idx = (e[1]^lastAnswer)%n
        if e[0] == 1:
            arr[idx].append(e[2])
        elif e[0] == 2:
            sar = len(arr[idx])
            lastAnswer = arr[idx][e[2] % sar]
            result.append(lastAnswer)
    return result

# output = [7,3]