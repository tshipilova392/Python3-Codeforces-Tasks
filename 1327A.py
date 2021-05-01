n = int(input())
for i in range(n):
    b,a = map(int,input().split())
    if b%2==1:
        if a%2==1:
            if b>=a*a:
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
    else:
        if a%2==0:
            if b>=a*a:
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
