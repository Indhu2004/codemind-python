n=int(input())
evencount=0
oddcount=0
r=0
while n>0:
    r=n%10
    if (r%2==0):
        evencount=evencount+1
    else:
        oddcount=oddcount+1
    n=n//10
if evencount==0:
    print("Odd")
elif oddcount==0:
    print("Even")
else:
    print("Mixed")