t = int(input())
for i in range(t):
    a,b,c = map(int,input().split())
    sum = a+b+c
    if sum%9!=0:
        print('NO')
    else:
        minEl = min(a,min(b,c))
        if minEl>=sum//9:
            print('YES')
        else:
            print('NO')