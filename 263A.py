'''
0 0 0 0 0
0 0 0 1 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
'''
p=[]
c=0
for a in range(5):
    p.append(input())
q=p[a].find("1")
if not q==-1:
    i=p.index("1")
    if i==2:
        pass
    if i<2:
        while i<2:
            i+=1
            c+=1
    if i>2:
        while i>2:
            i-=1
            c+=1
print(c)       
        