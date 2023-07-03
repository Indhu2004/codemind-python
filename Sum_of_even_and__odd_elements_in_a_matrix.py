r,c=map(int,input().split())
mat=[]
for i in range(r):
    lst=list(map(int,input().split()))
    mat.append(lst)
e=0
o=0
for i in range(r):
    for j in range(c):
        if mat[i][j]%2==0:
            e=e+mat[i][j]
        else:
            o=o+mat[i][j]
print(e,o)