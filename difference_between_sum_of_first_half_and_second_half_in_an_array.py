n=int(input())
a=list(map(int,input().split()))
b=n//2
d=a[:b]
e=a[b:]
f=sum(d)
g=sum(e)
print(g-f)