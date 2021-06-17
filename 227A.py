ax,ay = map(int,input().split())
bx,by = map(int,input().split())
cx,cy = map(int,input().split())
abx = bx-ax
aby = by-ay
bcx = cx-bx
bcy = cy-by
product = abx*bcy-aby*bcx
if product==0:
    print('TOWARDS')
elif product>0:
    print('LEFT')
else:
    print('RIGHT')