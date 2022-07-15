p=int(input())
t=[]
for i in range(p):
    a,b=map(int,input().split())
    if i==0:
        t.append(b-a)
    else:
        t.append(b-a+t[i-1])
print(max(t))