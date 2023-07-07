n=int(input())
lst=list(map(int,input().split()))
c=0
for i in lst:
    a=str(i)
    b=a[::-1]
    if a==b:
        c+=1
print(c)