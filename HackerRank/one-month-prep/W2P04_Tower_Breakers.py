# Week 2 Problem 4 - "Tower Breakers"
# Link - https://www.hackerrank.com/challenges/one-month-preparation-kit-tower-breakers-1/

# inputs:
# n = 2
# m = 6

def towerBreakers(n, m):
    if n%2==0 or m==1:
        return 2
    return 1


# output = 2