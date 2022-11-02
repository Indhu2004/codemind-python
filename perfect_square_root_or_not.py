n=int(input())
c=0
for i in range(1,1+n):
    a=i*i
    if a==n:
        c+=1
if c==1:
    print("True")
else:
    print("False")