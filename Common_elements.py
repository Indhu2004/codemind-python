n,m=map(int,input().split())
l=list(map(int,input().split()))
s=list(map(int,input().split()))
p=[]
for i in l:
    if i in s:
        p.append(i)
e=[]
for i in p:
    if i not in e:
        e.append(i)
print(*e)