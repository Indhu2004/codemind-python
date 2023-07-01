a=int(input())
for i in range(a):
    b=map(int,input().split())
    c=list(map(int,input().split()))
    d=list(map(int,input().split()))
    e=c+d
    f=sorted(e)
    print(*f)        