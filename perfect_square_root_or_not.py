n=int(input())
c=0
for i in range(n):
    if i*i==n:
        c=1
        break
if c==1:
    print("True")
else:
    print("False")