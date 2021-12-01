num = int(input(""))
i = 0
amountOfProblems = 0
problems = []
while i < num:
    i = i+1
    el = input("")
    problems.append(el)

for problem in problems:
    counterOfOnes = problem.count("1")
    if counterOfOnes > 1:
        amountOfProblems = amountOfProblems + 1
    else:
        pass

print(amountOfProblems)