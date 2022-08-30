# Problem - https://www.hackerrank.com/challenges/the-power-sum/
# Recursion

# inputs:
# X = 100
# N = 2

def powerSum(X, N, i=1):
    if X < 0 or X < i**N:
        return 0
    elif X == 0 or X == i**N:
        return 1
    return powerSum(X-i**N,N,i+1) + powerSum(X,N,i+1)

# output = 3