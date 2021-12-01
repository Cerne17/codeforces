def banana(initialCost, alreadyHaveMoney, bananaAmount):
    totalCost = initialCost * (2**bananaAmount - 1)
    toBorrow = totalCost - alreadyHaveMoney
    if toBorrow >= 0:
        return toBorrow
    else:
        return 0
string = input("")
array = string.split(" ")
k = int(array[0])
n = int(array[1])
w = int(array[2])
print(banana(k, n, w))