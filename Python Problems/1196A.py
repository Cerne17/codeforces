q=int(input(""))
i=0
x=[]
while i<q:
    i+=1
    r=input("")
    x.append(r)
for e in x:
    e=e.split()
    a=max(e)
    e.remove(a)
    a=int(a)
    b=min(e)
    e.remove(b)
    b=int(b)
    c=int(e[0])
    print("{}, {}, {}".format(a, b, c))