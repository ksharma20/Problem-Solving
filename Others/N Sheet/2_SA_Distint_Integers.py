# Sheet - https://docs.google.com/document/d/1eNleDHxWcgVUfRYLr0g8r1e-RbYVF7ri8ZUTYNYNR0w/edit?usp=sharing

# Given an array of integers and an integer K,
# find the number of subarrays with at least K distinct integers.
# Example 1:
# array = [1, 2, 1, 1] and k = 2
# output=2; {1,2} and {2,1} are only possibilities
# Example 2:
# array = [1, 2, 3, 4, 1] and k = 3
# output=6; {1, 2, 3}, {1, 2, 3, 4}, {1,2,3,4,1}, {2,3,4}, {2,3,4,1} and {3,4,1} are the only possibilities.
# Note that {1,2,3,4,1} is valid because it still has 3 distinct integers.

def checkUnique(arr):
    unique = 0
    s = []
    for e in arr:
        if e in s:
            unique -= 1
        else:
            unique += 1
            s.append(e)
    # print("unique == ", unique)
    return unique


def atLeastK(arr, k):
    left = count = 0
    right = k
    while right <= len(arr):
        # print(left, arr[left:right], right)

        if checkUnique(arr[left:right]) >= k:
            count += 1
        # print(count)
        if right - left > k+1:
            left += 1
            right -= 2
        elif right - left > k and right == len(arr):
            left += 1
            right -= 1

        right += 1

    return count


if __name__ == '__main__':
    array = [1, 2, 3, 4, 1]
    k = 3
    print(atLeastK(array, k))
