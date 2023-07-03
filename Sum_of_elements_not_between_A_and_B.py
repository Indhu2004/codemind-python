n=int(input())
lst=list(map(int,input().split()))
a,b=map(int,input().split())
e=0
for i in lst:
    if i<a or i>b:
        e=e+i
print(e)