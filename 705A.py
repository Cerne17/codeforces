listOfEmotions = ['I hate ', 'I love ']

n = int(input())
string=''

for i in range(n):
    if i != n-1:
        string+=listOfEmotions[i%2]
        string+='that'
        string+=' '
    else:
        string+=listOfEmotions[i%2]
        string+='it'
print(string)