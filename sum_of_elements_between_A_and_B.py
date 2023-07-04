n=int(input())
lst=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
d=0
for i in lst:
    if i>=a and i<=b:
        d=1
        c.append(i)
if d==1:
    print(sum(c))