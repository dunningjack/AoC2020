file = passwords

with open(file, 'r') as f:


for line in lines:
    pword.append((line.rsplit(":")))
    reqs.append((line.lsplit(":")))

for req in reqs:
    for i in range(0, len(req)):
        NumberOfInstances = req.lsplit(" ")
        LetterRequired = req.rsplit(" ")

for j in range(0, len(NumberOfInstances)):
