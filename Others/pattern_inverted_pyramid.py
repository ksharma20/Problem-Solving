# Input:
# Enter a Number: 22


space = 0
n = int(input("Enter a Number: "))
for _ in range(n//2 if n%2==0 else n//2+1):
    for _ in range(space):
        print(" ", end=' ')
    for _ in range(space, n-space):
        print("1", end=' ')
    space += 1
    print()


# Output:
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
#   1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
#     1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
#       1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
#         1 1 1 1 1 1 1 1 1 1 1 1 1 1
#           1 1 1 1 1 1 1 1 1 1 1 1
#             1 1 1 1 1 1 1 1 1 1
#               1 1 1 1 1 1 1 1
#                 1 1 1 1 1 1
#                   1 1 1 1
#                     1 1