n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(n):
    if l[i]==0 or l[i]==1:
        c=c+1
if c==len(l):
    print("True")
else:
    print("False")