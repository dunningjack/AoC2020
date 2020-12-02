file = "passwords"
pword = []
reqs = []
NumberOfInstances = []
LetterRequired = []
LowerLimit = []
UpperLimit = []

with open(file, 'r') as f:

    for line in f:
        pword.append((line.rsplit(":")))
        reqs.append((line.split(":", 1)))

    for req in reqs:
        for i in range(0, len(req)):
            NumberOfInstances.append(req[i].split(" ", 1))
            LetterRequired.append(req[i].rsplit(" "))

    for j in range(0, len(NumberOfInstances)):
        LowerLimit.append((NumberOfInstances[j].split("-", 1)))
        UpperLimit.append((NumberOfInstances[j].rsplit("-")))

    for k in range(0, len(pword)):
        if pword[k].count((LetterRequired[k])) == NumberOfInstances[k]:
            print(pword)
            break
        else:
            continue
