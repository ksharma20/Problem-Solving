 # Question: Reach the End and print the intermidiate Martix Values

# n = int(input())
n = 3
# walls = list(map(int, input().split(",")))
walls = [12,23]
# dirs = input()
dirs = "ESEESNSE"
dirs = list(dirs)

print("\nValue of N = ",n)
print("Walls = ",walls)
print("dirs = ",dirs)
print("__________\n")

output = []
# Output = [21, 22, 32, 22, 32, 33]

current = [1,1]
end = [n,n]

for v in dirs:
    print("current = ",current)
    print("value of V = ",v)
    print("__________")

    if current[0] == end[0] and current[1] == end[1]:
        break

    if v == "S":
        if current[0] == n:
            continue
        temp = current.copy()
        temp[0] = current[0] +1
        tv = int(str(temp[0])+str(temp[1]))
        print(tv)
        if tv in walls:
            continue
        else:
            current[0], current[1] = temp[0], temp[1]
            output.append(tv)
    elif v == "N":
        if current[0] == 1:
            continue
        temp = current.copy()
        temp[0] = current[0] -1
        tv = int(str(temp[0])+str(temp[1]))
        print(tv)
        if tv in walls:
            continue
        else:
            current[0], current[1] = temp[0], temp[1]
            output.append(tv)
    elif v == "E":
        if current[1] == n:
            continue
        temp = current.copy()
        temp[1] = current[1] +1
        tv = int(str(temp[0])+str(temp[1]))
        print(tv)
        if tv in walls:
            continue
        else:
            current[0], current[1] = temp[0], temp[1]
            output.append(tv)
    elif v == "W":
        if current[1] == 1:
            continue
        temp = current.copy()
        temp[1] = current[1] -1
        tv = int(str(temp[0])+str(temp[1]))
        print(tv)
        if tv in walls:
            continue
        else:
            current[0], current[1] = temp[0], temp[1]
            output.append(tv)


print("\n",output,"\n")