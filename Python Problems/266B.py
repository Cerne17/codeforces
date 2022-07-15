n,t=map(int,input().split())
q=str(input())
for i in range(0,t):
    if not q.find("BG") == -1:
        q=q.replace("BG", "GB")
print(q)