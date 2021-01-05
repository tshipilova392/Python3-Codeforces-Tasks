t=int(input())
for i in range(t):
    n = int(input())
    b=True
    mas = [int(x) for x in input().split()]
    for j in range(n-1):
        if abs(mas[j]-mas[j+1])%2==1:
            print("NO")
            b = False
            break
    if b:
        print("YES")