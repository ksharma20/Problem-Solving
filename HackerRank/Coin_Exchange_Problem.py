# Problem - https://www.hackerrank.com/challenges/coin-change/
# Dynamic Programming

# inputs:
# n = 3
# coins = [8,3,2,1]

def getWays(n, c):
    ways = [1] + [0]*n
    for coin in c:
        # print("coin = ",coin)
        if n >= coin:
            for i in range(coin,n+1):
                # print("i = ",i)
                ways[i] += ways[i-coin]
                # print(f"ways[{i}] = {ways[i]}")
        # print(ways)
    return ways[n]

# output = 3