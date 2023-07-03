n=int(input())
lst=list(map(int,input().split()))
e=0
o=0
for i in lst:
    if i%2==0:
        e+=i
    else:
        o+=i
if e>o:
    print(e-o)
else:
    print(o-e)