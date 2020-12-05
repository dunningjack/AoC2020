from typing import List

file = "Passports"
PP = []
validPP = 0

PP_dict = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}
PP_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']


with open(file, "r") as f:
    line = f.readline()

    def addPP():
        for line in f:
            while line != "\n":
                PP.append(line)
        return PP

    def validatePP(validPP):
        for i in range(0, len(PP)):
            check = any(item in PP_keys for item in PP[i])
            if check is True:
                validPP += 1
        return validPP

    addPP()
    validPP
print(validPP)