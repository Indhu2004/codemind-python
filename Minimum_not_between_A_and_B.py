n=int(input())
lst=list(map(int,input().split()))
a,b=map(int,input().split())
d=0
l=[]
for i in lst:
    if i<a or i>b:
        d=1
        l.append(i)
if d==1:
    print(min(l))
else:
    print(-1)