def binarySearch(nums,target):
    if len(nums) == 0:
        return -1
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > target:
            right = mid
        else:
            left = mid + 1
    return left

n = int(input())
a = list(map(int,input().split()))
m = int(input())
q = list(map(int,input().split()))
s = []
sum=0
for i in range(n):
    sum+=a[i]
    s.append(sum)
for i in range(n):
    s[i]+=1
for i in range(m):
    print(binarySearch(s,q[i])+1)