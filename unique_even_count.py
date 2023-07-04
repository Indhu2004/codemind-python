n=int(input())
l=list(map(int,input().split()))
k=[]
c=0
for i in l:
    if i%2==0:
        k.append(i)
b=set(k)
for i in b:
    if i%2==0:
        c=c+1
print(c)