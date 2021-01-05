n = int(input())
s = input()
m = []
for i in range(1, n):
	m.append(s[i-1] + s[i])
m.sort()
max = 0
kol=1
for i in range(n-2):
    if m[i]==m[i+1]:
        kol+=1
    else:
        if kol>max:
            max = kol
            smax = m[i]
        kol=1
if kol>max:
    max = kol
    smax = m[n-3]
print(smax)