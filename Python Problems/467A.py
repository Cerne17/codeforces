'''
number of rooms
p q
q has to be AT LEAST two units greater than p
'''
n=int(input())
z=0
for i in range(n):
    a,b=map(int, input().split())
    b=b-2
    if b>=a:
        z+=1
print(z)