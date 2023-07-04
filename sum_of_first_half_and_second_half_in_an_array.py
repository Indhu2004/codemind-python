n=int(input())
a=list(map(int,input().split()))
b=n//2
d=a[:b]
e=a[b:]
print(sum(d))
print(sum(e))