A = [0,4]
N = 2

def max_pair(A: list, n:int):
    B = [ [ 0 for _ in range(n) ] for _ in range(n) ]
    # print(B)
    for i in range(n):
        xor = A[i]
        # print("i = ",i)
        for j in range(i,n):
            # print("j = ",j)
            xor ^= A[j]
            # print(f" xor = {xor} ")
            B[i][j] = xor
            # print(f" B[{i}][{j}] = {B[i][j]} ")

    C1 = 0
    rowB = 0
    for i,b in enumerate(B):
        if C1 < max(b):
            C1 = max(b)
            rowB = i
    B[rowB].remove(C1)
    C2 = max([max(b) for b in B ])
    
    return C1+C2

print(max_pair(A,N))
            
    