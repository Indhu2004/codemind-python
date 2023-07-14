a,b=map(int,input().split())
c=str(a)
d=c[0:b]
e=c[-b:]
print(abs(int(d)-int(e)))