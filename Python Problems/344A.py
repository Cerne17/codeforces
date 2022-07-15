n, a, counter = int(input()), [], 1
for i in range(n):
    a.append(input())
for e in range(n-1):
    if not a[e]==a[e+1]:
        counter+=1
print(counter)