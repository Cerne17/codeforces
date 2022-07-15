n=int(input(""))
i=0
l=[]
while i<n:
    i+=1
    e=input("")
    l.append(e)
for case in l:
    k=0
    m = case.split()
    a=int(m[0])
    b=int(m[1])
    c=int(m[2])
    while a<=c and b<=c:
        k+=1
        if a<b:
            a+=b
        else:
            b+=a
    print(k)