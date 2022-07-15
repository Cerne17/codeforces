'''
inputs:
    number of friends
    ith term stands for the amount of presents this person gave
outputs:
    ith number stands for the number of the friend that gave them a present
EACH PERSON RECIEVED ONE PRESENT
'''
n, p, d = int(input()), input().split(), {}
for i in range(n):
    i+1
    d.update({f"a{i}":"0"})
for i in range(n):
    a=i+1
    d[f"a{a}"]=p[i]
print(d)