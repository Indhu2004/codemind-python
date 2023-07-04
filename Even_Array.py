n=int(input())
l=list(map(int,input().split()))
d=[]
for i in range(n):
    if l[i]%2==0:
        d.append(i)
if len(d)==n:
    print("True")
else:
    print("False")