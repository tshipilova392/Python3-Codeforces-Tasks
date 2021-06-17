t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    if n%2==0:
       if k%n==0:
           print(n)
       else:
           print(k%n)
    else:
        if k%n==0:
            x1 = n
        else:
            x1 = k%n
        x1+=(k-1)//(n//2)
        if (x1%n==0):
            print(n)
        else:
            print(x1%n)