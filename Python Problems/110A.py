n=str(input())
n4=int(n.count("4"))
n7=int(n.count("7"))
m=n4+n7
if m==4 or m==7:
    print("YES")
else:
    print("NO")