s=int(input())
d=list(map(int,input().split()))
ev=0
od=0
for i in range(s):
    if i%2==0:
        ev=ev+d[i]
    else:
        od=od+d[i]
t=ev-od
if t==0:
    print("YES")
else:
    print("NO")