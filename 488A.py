def hasEight(x):
    s = str(x)
    if '8' in s:
        return(True)
    else:
        return(False)
a = int(input())
amount=0
while (True):
    a+=1
    amount+=1
    if (hasEight(a)):
        print(amount)
        break