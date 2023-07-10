n=int(input())
l=list(map(int,input().split()))
c=0
min=99
for i in l:
    if len(str(i))<min:
        min=len(str(i))
for i in l:
    if len(str(i))==min:
        c=c+1
print(c)
    
