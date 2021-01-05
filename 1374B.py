n = int(input())
for i in range(n):
    kol = 0
    x = int(input())
    b = True
    while x != 1:
        if x % 3 != 0:
            print(-1)
            b = False
            break
        if x % 2 == 0:
            kol += 1
            x = x//6
            continue
        if x % 2 != 0:
            kol += 2
            x = x//3
    if b:
        print(kol)