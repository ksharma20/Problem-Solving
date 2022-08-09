# Week 2 Problem 12 - "Counter game"
# Link - https://www.hackerrank.com/challenges/one-month-preparation-kit-counter-game/

# inputs:
# n = 6

def counterGame(n):
    if n == 1:
        return "Richard"
    elif n == 2:
        return "Louise"
    else:
        c = 0
        while n!=1:
            c += 1
            # print("n = ",n)
            log_n = math.log2(n)
            # print("log_n = ",log_n)
            if log_n == 1:
                break
            elif log_n.is_integer():
                n = int(n/2)
            else:
                n = n - 2**(int(log_n))
            
    
    return "Richard" if c%2==0 else "Louise"

# output = "Richard"