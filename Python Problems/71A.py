numberOfInputs = int(input(""))
i=0
inputs = []
while i < numberOfInputs:
    i = i+1
    alpha = input("")
    inputs.append(alpha)
for element in inputs:
    elementLen = len(element)
    if elementLen > 10:
        word = element
        wordFirst = str(word[0])
        wordlast = str(word[-1])
        element = str(len(element) - 2)
        element = wordFirst + element + wordlast
    else:
        pass
    print(element)
