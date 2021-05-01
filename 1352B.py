t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    if k>n:
        print('NO')
        continue
    if k==n:
        print('YES')
        print('1 '*n)
        continue
    if (n%2==1)and(k%2==0):
        print('NO')
        continue
    if (n % 2 == 1) and (k % 2 == 1):
        print('YES')
        print('1 '*(k-1)+str(n-k+1))
        continue
    if (n % 2 == 0):
        if (k<=n//2):
            print('YES')
            print('2 '*(k-1)+str(n-(k-1)*2))
        else:
            if (k%2==1):
                print('NO')
            else:
                print('YES')
                print('1 ' * (k - 1) + str(n - k + 1))