t = int(input())
for i in range(t):
   n,m = map(int,input().split())
   s = 'W'+'B'*(m-1)
   print(s)
   s = 'B'*m
   for j in range(n-1):
       print(s)