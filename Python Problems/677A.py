n,h=map(int, input().split())
m=input().split()
a=[]
b=0
for i in range(n):
    z=int(m[i])
    if z>h:
        c=2
        a.append(c)
    else:
        c=1
        a.append(c)
for i in a:
    b+=i
print(b)