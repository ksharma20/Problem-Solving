# Week 2 Problem 3 - "Drawing Book"
# Link - https://www.hackerrank.com/challenges/one-month-preparation-kit-drawing-book/

# inputs:
# n = 5
# p = 3

def pageCount(n, p):
    turns = 0
    if n-p <= p-1:
        if n%2==0:
            page = n
        else:
            page = n-1
        while p < page:
            turns += 1
            page -= 2
    else:
        page = 1
        while p > page:
            turns += 1
            page += 2
            
    return turns

# output = 1