n = int(input())
for i in range(n):
    t = input()
    if ('0' in t)and('1' in t):
        print('01'*len(t))
    else:
        if ('0' in t):
            print('0'*len(t))
        else:
            print('1'*len(t))
