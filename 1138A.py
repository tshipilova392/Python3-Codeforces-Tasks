t=int(input())
mas = [int(x) for x in input().split()]
k=1
lengths = []
for i in range(t-1):
    if (mas[i]==mas[i+1]):
        k+=1
    else:
        lengths.append(k)
        k=1
lengths.append(k)
max =0
for i in range(len(lengths)-1):
    if min(lengths[i],lengths[i+1])>max:
        max = min(lengths[i],lengths[i+1])
print(max*2)