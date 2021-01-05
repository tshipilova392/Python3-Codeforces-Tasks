n , m = map(int, input().split())
kol = n
days = 0
while kol>0:
    kol -= 1
    days += 1
    if days % m ==0:
        kol += 1
print(days)