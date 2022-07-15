p=list(input())
a=[]
t=''
s=p.count("+")
for i in range(s):
    p.remove("+")
p.sort()
for e in p[0:-1]:
    t=t+e+"+"
t=t+p[-1]
print(t)