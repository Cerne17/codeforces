a=input()
b=list(a)
b.sort()
l=int(len(a)/2)
c=str(b[l]).isupper()
if c == True:
    print(a.upper())
else:
    print(a.lower())