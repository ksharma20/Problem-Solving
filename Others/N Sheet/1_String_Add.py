# Sheet - https://docs.google.com/document/d/1eNleDHxWcgVUfRYLr0g8r1e-RbYVF7ri8ZUTYNYNR0w/edit?usp=sharing

# Given two strings a and b we need to add ith elements from both.
# Time limit 0.5secs (AFAIR). (Input size limits I do not remember)
# Eg1:
# a = "99"
# b = "99"
# ans = "1818"
# Eg2:
# a = "9"
# b = "11"
# ans = "110"

def add(s1: str, s2: str) -> str:
    sl1 = len(s1)
    sl2 = len(s2)
    if sl1 > sl2:
        s2 = "0"*(sl1-sl2) + s2
    elif sl1 < sl2:
        s1 = "0"*(sl2-sl1) + s1
    res = ""
    for a, b in zip(s1, s2):
        res += f"{int(a)%10 + int(b)%10}"
    return res


if __name__ == '__main__':
    input1 = "9"
    input2 = "11"
    print(add(input1, input2))
