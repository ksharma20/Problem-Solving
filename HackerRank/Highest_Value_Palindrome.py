# Problem - https://www.hackerrank.com/challenges/richie-rich/
# Recursion

# inputs:
# s = '092282'
# n = 6
# k = 3

def highestValuePalindrome(s, n, k):
    s = list(s)
    
    changed = [0]*n
    
    left = 0
    right = n-1
    
    # Making the String to Palindrome 
    while left <= right:
        if s[left] != s[right]:
            if s[left] > s[right]:
                s[right] = s[left]
                changed[right] = 1
            else:
                s[left] = s[right]
                changed[left] = 1
            k -= 1
        
        left += 1
        right -= 1
            
    if k < 0:
        return "-1"
    
    left = 0
    right = n-1
    
    # Maximing Palindrome 
    while left <= right:
        if left == right and k > 0:
            s[left] = '9'
            break
        elif s[left] != '9':
            if (changed[left] or changed[right]) and k > 0:
                s[left] = s[right] = '9'
                k -= 1
            elif not (changed[left] or changed[right]) and k > 1:
                s[left] = s[right] = '9'
                k -= 2
                
        left += 1
        right -= 1
        
    return "".join(s)

# output = '992299'