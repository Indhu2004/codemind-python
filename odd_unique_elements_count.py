n=int(input())
l=list(map(int,input().split()))
c=0
k=[]
for i in l:
    if i not in k:
        k.append(i)
for i in k:
    if i%2!=0:
        c=c+1
print(c)