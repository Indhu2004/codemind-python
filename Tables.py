n,r=map(int,input().split())
i=1
for i in range(1,r+1):
    if(i%2!=0):
        a=n*i
        print(n,"x",i,"=",a)