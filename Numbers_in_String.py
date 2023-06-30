s=input()
c="".join(s)
c1=list(c)
b=0
for i in c1:
    if i.isdigit():
        b+=int(i)
print(b)
        