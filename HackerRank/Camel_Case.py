# Problem - https://www.hackerrank.com/challenges/camelcase/

# inputs:
# s = 'saveChangesInTheEditor'

def camelcase(s):
    count = 1
    for c in s:
        if c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            count += 1
    return count

# output = 5