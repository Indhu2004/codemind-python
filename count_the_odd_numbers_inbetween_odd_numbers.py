n=int(input())
lst=list(map(int,input().split()))
e=0
for i in range(1,len(lst)-1):
    if lst[i]%2!=0:
        if lst[i-1]%2!=0 and lst[i+1]%2!=0:
            e+=1
print(e)