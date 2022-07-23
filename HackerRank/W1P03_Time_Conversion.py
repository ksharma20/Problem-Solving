# Week 1 Problem 3 - "Time Conversion"
# Link - https://www.hackerrank.com/challenges/one-month-preparation-kit-time-conversion/

# inputs
# s = "07:05:45PM"

def timeConversion(s):
    dt = s.split(':')
    # print(dt)
    if dt[0] == '12' and dt[2][2] == 'A':
        dt[0] = '00'
    elif dt[2][2] == 'P' and dt[0] != '12':
        dt[0] = str(int(dt[0])+12)
    
    return dt[0]+":"+dt[1]+":"+dt[2][0:2]

# output = "19:05:45"