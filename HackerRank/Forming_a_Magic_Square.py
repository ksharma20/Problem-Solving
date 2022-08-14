# Problem - https://www.hackerrank.com/challenges/magic-square-forming/

# inputs:
# s = [[5, 3, 4],
# [1, 5, 8],
# [6, 4, 2]]

def formingMagicSquare(s):
    posibilities = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]], 
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]], 
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
    ]
    costs = []
    
    for p in posibilities:
        cost = 0
        for prow, srow in zip(p,s):
            for pcol, scol in zip(prow,srow):
                if pcol != scol:
                    cost += abs(pcol-scol)
        costs.append(cost)
    
    return min(costs)

# output = 7