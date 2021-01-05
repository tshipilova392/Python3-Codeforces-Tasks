na, nb = map(int, input().split())
k, m = map(int, input().split())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
t1 = a[k-1]
t2 = b[-m]
print("YES" if t1<t2 else "NO")