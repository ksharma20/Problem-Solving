# Problem - https://www.hackerrank.com/challenges/extra-long-factorials/

# inputs:
# n = 25

def extraLongFactorials(n):
    lf = 1
    for i in range(n,1,-1):
        lf *= i
    print(lf)

# output = 15511210043330985984000000