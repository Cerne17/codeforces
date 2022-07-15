a, b = map(int, input().split())
counter=0
while a<=b:
    counter+=1
    a=3*a
    b=2*b
print(counter)