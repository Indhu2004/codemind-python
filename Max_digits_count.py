n=int(input())
l=list(map(int,input().split()))
c=0
max=0
for i in l:
    if len(str(i))>max:
        max=len(str(i))
for i in l:
    if len(str(i))==max:
        c=c+1
print(c)
    