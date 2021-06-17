r,d = map(int,input().split())
r1 = r-d
r2=r
n = int(input())
k = 0
for i in range(n):
    x,y,ri = map(int,input().split())
    if (x*x+y*y>=(r1+ri)**2)and(x*x+y*y<=(r2-ri)**2):
        k+=1
print(k)