n=int(input())
lst=list(map(int,input().split()))
ev=0
od=0
for i in range(len(lst)):
    if i%2==0:
        ev=ev+lst[i]
    else:
        od=od+lst[i]
print(ev-od)