# Problem - https://www.hackerrank.com/challenges/stone-division-2/

# inputs:
# n = 12
# s = [2,3,4]

# Recursive Way (Does not pass all test cases)
def stoneDivision(n, s):
    print(n,s)
    s.sort(reverse=True)
    if n < 2:
        return 0
    
    maxMoves = 0
    
    for x in s:
        moves = 0
        if n%x == 0 and n !=x:
            moves += stoneDivision(x,s) * (n//x) +1
        maxMoves = max(maxMoves, moves)
    
    print("Moves = ",maxMoves)
    return maxMoves

# output = 4