n,a,counter=int(input()),input().split(),0
for i in range(n):
    if a[i]=='1':
        counter+=1
if counter>0:
    print("HARD")
else:
    print("EASY")