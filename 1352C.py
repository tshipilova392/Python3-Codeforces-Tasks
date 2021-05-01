n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    kolBlocks = b//(a-1)
    if b%(a-1)!=0:
        print(kolBlocks*a+b%(a-1))
    else:
        print(kolBlocks * a - 1)
