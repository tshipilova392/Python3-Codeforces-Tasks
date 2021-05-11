n = int(input())
a = list(map(int, input().split()))
b = list(map(lambda x: -1 if x==1 else 1, a))
sum=0
startIndex = 0
ind=0
endIndex=0
max =0
for i in range(len(b)):
    sum+=b[i]
    if sum>max:
        max=sum
        endIndex=i
        startIndex = ind
    if sum<0:
        sum=0
        ind=i+1
for i in range(startIndex,endIndex+1):
    a[i]=1-a[i]
if startIndex==len(b):
    a[0]=1-a[0]
kol=0
for i in range(len(a)):
    if (a[i]==1):
        kol+=1
print(kol)
