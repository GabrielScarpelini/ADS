p, n = input().split()
p = int(p)
n = int(n)
canos = input().split()

for i in range(len(canos)):
    canos[i] = int(canos[i])

length = abs(canos[1] - canos[0])

for i in range(len(canos)):
    if p < length:
        print('GAME OVER')
        break
    elif i == len(canos)-1:
        print('YOU WIN')
    else: length = abs(canos[i+1] - canos[i])
