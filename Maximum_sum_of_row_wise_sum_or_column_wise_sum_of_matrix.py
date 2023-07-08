r,c=map(int,input().split())
mat=[]
for i in range(r):
    l=list(map(int,input().split()))
    mat.append(l)
b=[]
for i in range(r):
    b.append(sum(mat[i]))
print(max(b))