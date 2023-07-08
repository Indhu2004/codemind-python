n=int(input())
l=list(map(int,input().split()))
for i in l:
    a=str(i)
    b=a[::-1]
    print(int(b),end=" ")