n=int(input())
lst=list(map(int,input().split()))
o=[]
e=[]
for i in lst:
    if i%2==0:
        e.append(i)
    if i%2!=0:
        o.append(i)
print(*o,*e)