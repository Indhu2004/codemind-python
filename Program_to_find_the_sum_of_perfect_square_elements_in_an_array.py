import math
def sq(x):
    if x>=0:
        s=int(math.sqrt(x))
        if s*s==x:
            return True
    return False
n=int(input())
s=list(map(int,input().split()))
c=0
for i in s:
    if sq(i):
        c+=i
print(c)
        