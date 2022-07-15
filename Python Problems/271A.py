n=int(input())
n+=1
m=len(set(str(n)))
while not m == 4:
    n=int(n)
    n+=1
    m=len(set(str(n)))
print(n)