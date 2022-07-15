'''
Initial X = 0

check for "--" or "++" in the input
if ++: x+=1
if --: x-=1

'''
x=0
n=int(input())
for i in range(n):
    p=input()
    if p.find("++") == -1:
        x-=1
    if p.find("--") == -1:
        x+=1
print(x)