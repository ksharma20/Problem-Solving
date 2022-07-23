# Week 1 Problem 4 - "Sparse Array"
# Link - https://www.hackerrank.com/challenges/one-month-preparation-kit-sparse-arrays/

# inputs:
# strings = ["aba","baba","aba","xzxb"]
# queries = ["aba","xzxb","ab"]

def matchingStrings(strings, queries):
    result = []
    for q in queries:
        count = 0
        for s in strings:
            if q == s:
                count += 1
        result.append(count)
        count = 0
    return result

# output = [2,1,0]