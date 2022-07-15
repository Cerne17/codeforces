a=input().lower()
b=input().lower()
c=[a,b]
d=1
if a==b:
   d=0
else:
    c.sort()
    if c[0]==a:
        d='-1'
print(d)