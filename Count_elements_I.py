n,m=map(int,input().split())
l=list(map(int,input().split()))
s=list(map(int,input().split()))
p=[]
for i in l:
    for j in s:
        if i==j:
            p.append(j)
d=set(p)
print(len(d))
