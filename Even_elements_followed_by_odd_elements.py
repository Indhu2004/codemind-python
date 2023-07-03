n=int(input())
lst=list(map(int,input().split()))
e=[]
o=[]
for i in lst:
    if i%2==0:
        e.append(i)
    if i%2!=0:
        o.append(i)
print(*e,*o)