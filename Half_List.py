n=int(input())
d=list(map(int,input().split()))
a=n//2
c=d[a:]
e=d[:a]
b=c[::-1]
print(*b,*e)