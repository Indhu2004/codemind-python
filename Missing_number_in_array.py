a=int(input())
for i in range(a):
    b=int(input())
    c=list(map(int,input().split()))
    d=0
    for i in range(1,b+1):
        if i not in c:
            d=i
    print(d)
        