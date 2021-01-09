t=int(input())
for i in range(t):
    n = int(input())
    s = input()
    oddAmount = 0
    evenAmount = 0
    if n % 2 != 0:
        for j in range(0, n, 2):
            if int(s[j]) % 2 == 1:
                oddAmount += 1
            else:
                evenAmount += 1
        if oddAmount > 0:
            print(1)
        else:
            print(2)
    else:
        for j in range(1, n, 2):
            if int(s[j]) % 2 == 1:
                oddAmount += 1
            else:
                evenAmount += 1
        if evenAmount > 0:
            print(2)
        else:
            print(1)