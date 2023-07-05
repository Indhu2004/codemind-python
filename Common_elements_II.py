n,m=map(int,input().split())
l=list(map(int,input().split()))
s=list(map(int,input().split()))
p=[]
for i in l:
    if i not in s:
        p.append(i)
for j in s:
    if j not in l:
        p.append(j)
print(*p)