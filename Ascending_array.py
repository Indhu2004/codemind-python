n=int(input())
l=list(map(int,input().split()))
d=set(l)
e=sorted(d)
if l==e:
    print("yes")
else:
    print("no")