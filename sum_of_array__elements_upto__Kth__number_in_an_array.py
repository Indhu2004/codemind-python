n=int(input())
l=list(map(int,input().split()))
k=int(input())
d=[]
for i in l:
    if i<=k:
        d.append(i)
print(sum(d))
        