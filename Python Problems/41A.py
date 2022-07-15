a=input()
b=list(input())
b=b[::-1]
c=""
for i in b:
    c+=i
if a==c:
    print("YES")
else:
    print("NO")