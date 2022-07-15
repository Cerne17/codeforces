'''
k = cost of the first banana
n = initial money
w = amount of bananas
b = borrowed money
t = totalPrice
total price:
    1*k + 2*k + 3*k + 4*k + 5*k + 6*k + ... + w*k
'''
t = 0
k, n, w = map(int, input("").split())
for i in range(0, w):
    t += (i+1)*k
b=t-n
if b<0:
    b=0
print(b)