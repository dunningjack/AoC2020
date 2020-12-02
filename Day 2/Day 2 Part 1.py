file = "passwords"
lines = dict
pword = []
reqs = []
NumberRange = []
LowerLimit = []
UpperLimit = []

with open(file, 'r') as f:

    for line in f:
        # line.rstrip("\n")
        lines[line] = (line.split(": "))

    for i in range(0, len(reqs)):
        reqs.append(lines[i][0])
        pword[i].append(lines[i][1])

    for j in range(0, len(pword)):
        LowerLimit.append(reqs.partition(""))