'''
Inputs:
1- Number of drinks
2- The percentage of OJ in each drink, each one separated by a space
The Logic:
Compute the Arithmetic Mean of the numbers in the second input and printing it.
'''

div = int(input())
_sum=0
_list=input().split()
for element in _list:
    _sum+=int(element)
result=_sum/div
print(result)
