import math
n = int(input())
sum=n
x = n
while (x!=1):
    f = True
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            x=x//i
            f = False
            break
    if f:
        x = 1
    sum+=x
print(sum)