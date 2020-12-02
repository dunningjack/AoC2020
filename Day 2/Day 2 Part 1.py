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
        reqs.append((line.lsplit(":")))

    for req in reqs:
        for i in range(0, len(req)):
            NumberOfInstances.append(req.lsplit(" "))
            LetterRequired.append(req.rsplit(" "))

    for j in range(0, len(NumberOfInstances)):
        LowerLimit.append(NumberOfInstances[j].lsplit("-"))
        UpperLimit.append(NumberOfInstances[j].rsplit("-"))

    for k in range(0,len(pword)):
        if pword[k].count(LetterRequired[k]) == NumberOfInstances[k]:
            print(pword)
            break
        else:
            continue
