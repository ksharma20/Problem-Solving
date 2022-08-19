# Problem - https://www.codingame.com/ide/puzzle/shadows-of-the-knight-episode-1
# Skills Needed: Binary Search & Intervals

w, h = [int(i) for i in input().split()] # w: width of the building. h: height of the building.
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

# print(w,h,n, file=sys.stderr, flush=True)
# print(x0,y0, file=sys.stderr, flush=True)

ws = 0
hs = 0
we = w-1
he = h-1
# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    # print(bomb_dir, file=sys.stderr, flush=True)
    # print(ws,we,"\t",hs,he, file=sys.stderr, flush=True)
    
    if bomb_dir == 'U':
        he = y0
        if y0-hs == 1:
            y0 -= 1
        else: y0 = hs + (y0-hs)//2

    elif bomb_dir == 'UR':
        ws = x0
        if we-ws == 1:
            x0 += 1
        else: x0 += (we-ws)//2
        he = y0
        if y0-hs == 1:
            y0 -= 1
        else: y0 = hs + (y0-hs)//2
    
    elif bomb_dir == 'R':
        ws = x0
        if we-ws == 1:
            x0 += 1
        else: x0 += (we-ws)//2
    
    elif bomb_dir == 'DR':
        ws = x0
        if we-ws == 1:
            x0 += 1
        else: x0 += (we-ws)//2
        hs = y0
        if he-hs == 1:
            y0 += 1
        else: y0 += (he-hs)//2
    
    elif bomb_dir == 'D':
        hs = y0
        if he-hs == 1:
            y0 += 1
        else: y0 += (he-hs)//2
    
    elif bomb_dir == 'DL':
        we = x0
        if x0-ws == 1:
            x0 -= 1
        else: x0 = ws + (x0-ws)//2
        
        hs = y0
        if he-hs == 1:
            y0 += 1
        else: y0 += (he-hs)//2
    
    elif bomb_dir == 'L':
        we = x0
        if x0-ws == 1:
            x0 -= 1
        else: x0 = ws + (x0-ws)//2
    
    elif bomb_dir == 'UL':
        we = x0
        if x0-ws == 1:
            x0 -= 1
        else: x0 = ws + (x0-ws)//2
        he = y0
        if y0-hs == 1:
            y0 -= 1
        else: y0 = hs + (y0-hs)//2


    print(x0,y0)
