a=int,input()
l=list(map(int,input().split()))
for i in l:
    if i<0:
        i=-i
    d=str(i)
    print(len(d),end=" ")