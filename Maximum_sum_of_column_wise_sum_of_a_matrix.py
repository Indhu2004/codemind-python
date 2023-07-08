r,c=map(int,input().split())
mat=[]
for i in range(r):
    lst=list(map(int,input().split()))
    mat.append(lst)
l=[]
for i in range(c):
    d=0
    for j in range(r):
        d=d+mat[j][i]
    l.append(d)
print(max(l))
        