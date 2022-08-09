# # Problem - https://www.hackerrank.com/challenges/flatland-space-stations/

# inputs:
# n = 5
# c = [0,4]

def flatlandSpaceStations(n, c):
    maxDis = 0
    for i in range(n):
        maxDis = max(maxDis, min( [ abs(i-e) for e in c] ))
    return maxDis

# Note - This Does not passes test case 15 & 16

# output = 2