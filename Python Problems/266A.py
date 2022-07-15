'''
        TEST CASES
def function(n, stones):

    counter = 0

    for i in range(1, n):
        if stones[i] == stones[i-1]:
            counter+=1
    return counter


def test_exemple1():
    result = function(3, "RGB")
    assert result == 1


def test_exemple2():
    result = function(5, "RRRRR")
    assert result == 4


def test_exemple3():
    result = function(4, "BRBG")
    assert result == 0
'''

'''
        SOLUTION
'''
n = int(input())
stones = input()

counter = 0

for i in range(1, n):
    if stones[i] == stones[i-1]:
        counter+=1
        
print(counter)