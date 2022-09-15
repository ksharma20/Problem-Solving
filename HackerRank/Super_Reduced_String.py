# Problem - https://www.hackerrank.com/challenges/reduced-string/

# inputs:
# s = 'aaabccddd'

def superReducedString(s):
    result = []
    for c in s:
        if result:
            if c == result[-1] :
                result.pop()
                continue
        result.append(c)
    return ''.join(result) if result else 'Empty String'

# output = 'abd'