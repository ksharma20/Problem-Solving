# Problem: A XOR Operation 
# Link - https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/practice-problems/algorithm/strange-xor-2-fc8ad535/

# You are given a set S of distinct positive integers of size n (n is always even). 
# Print the minimum positive integer k that is greater than 0 
# such that after replacing each element e of the set s with e^k, 
# set S remains the same.

# Print -1 if there is no such k.

# Note: It is guaranteed that  is odd.

# Input format :
# The first line contains a single integer  denoting the number of test cases.
# The first line of each test case contains a single integer  denoting the number of elements in the set.
# The second line of each test case contains  integers .
# Output format

# Print  lines each containing a single line that contains .

# Sample Input
# 1
# 6
# 5 6 9 10 13 14
# Sample Output
# 3

# Time Limit: 2
# Memory Limit: 256
# Source Limit:
# Explanation
# By performing the XOR of k with each element we get the given set S

# 5⊕3=6

# 6⊕3=5

# 13⊕3=14

# 14⊕3=13

# 9⊕3=10

# 10⊕3=9

# S' = {6,5,14,13,10,9} which is same as S={5,6,13,14,9,10}


t = int(input())
for _ in range(t):
    n = int(input())
    vset = set(map(int,input().split()))
    k = 0
    for e in vset:
        k ^= e
    for e in vset:
        if e^k not in vset:
            print(-1)
            break
    else:
        print(k)
        break