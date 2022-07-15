c=0
n, k = map(int, input().split())
k-=1
s = list(input().split())
for i in range(n):
    a=int(s[i])
    b=int(s[k])
    if a==0:
        break
    elif a>=b:
        c+=1
print(c)