n=int(input())
l=list(map(int,input().split()))
d=set(l)
e=sorted(d)
f=e[::-1]
if l==f:
    print("yes")
else:
    print("no")