a=input()
b='abcdefghijklmnopqrstuvwxyz1234567890 '
c=a.lower()
d=0
for i in c:
    if i not in b:
        d=d+1
print(d)