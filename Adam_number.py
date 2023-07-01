def rev(n):
    d=0
    while n!=0:
        r=n%10
        d=d*10+r
        n=n//10
    return d
n=int(input())
t=n*n
s=rev(n)
b=s*s
if rev(b)==t:
    print("True")
else:
    print("False")