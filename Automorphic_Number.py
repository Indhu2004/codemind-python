n=int(input())
d=n*n
flag=0
while n>0:
    if n%10!=d%10:
        print("Not an Automorphic Number")
        flag=1
        break
    n=n//10
    d=d//10
if flag==0:
    print("Automorphic Number")