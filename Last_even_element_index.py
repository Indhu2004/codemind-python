n=int(input())
arr=list(map(int,input().split()))
for i in range(len(arr)):
    if arr[i]%2==0:
        c=i
print(c)