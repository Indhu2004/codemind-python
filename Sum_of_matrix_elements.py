r=int(input())
c=int(input())
mat=[]
for i in range(r):
    a=list(map(int,input().split()))
    mat.append(a)
rsum=[]
for i in range(r):
    rsum.append(sum(mat[i]))
print(sum(rsum))