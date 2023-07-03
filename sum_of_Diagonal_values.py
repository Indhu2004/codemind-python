r,c=map(int,input().split())
mat=[]
for i in range(r):
    lst=list(map(int,input().split()))
    mat.append(lst)
h=[]
for i in range(r):
    for j in range(c):
        if i==j or i+j==r-1:
            h.append(mat[i][j])
print(sum(h))