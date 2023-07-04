n=int(input())
l=list(map(int,input().split()))
b=sum(l)
c=b//n
d=0
for i in range(n):
    if l[i]>=c:
        d=d+1
print(d)
        