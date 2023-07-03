r,c=map(int,input().split())
mat=[]
for i in range(r):
    lst=list(map(int,input().split()))
    mat.append(lst)
e=[]
o=[]
for i in range(r):
    if i%2==0:
        e.append(sum(mat[i]))
    else:
        o.append(sum(mat[i]))
print(sum(e),sum(o))