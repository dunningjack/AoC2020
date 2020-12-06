file = "Passports"
PP = []

PP_dict = {'byr':[], 'iyr':[], 'eyr':[], 'hgt':[], 'hcl':[], 'ecl':[], 'pid':[], 'cid':[]}
PP_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid',]

with open(file, "r") as f:
    lines = f.readlines()


    def addPP():
        x = 0
        PP.append("")
        for i in range(0, len(lines)):
            if lines[i] != "\n":
                PP[x] += lines[i].strip() + " "
            else:
                x += 1
                PP.append("")
        return PP

    PP = addPP()

    def validatePP():
        validPP = 0
        for i in range(0, len(PP)):
            count = 0
            for j in range(0, len(PP_keys)):
                if PP_keys[j] in PP[i]:
                    count += 1
            if count == 7:
                validPP += 1

        return validPP

    validPP = validatePP()

    def checkEntries():
        for i in range(0, len(PP)):
            splitPP = PP[i].split(" ")
            for j in range(0, len(splitPP)):
                checkkey = splitPP[j].split(":", 0)
                checkvalue = splitPP[j].split(":", 1)
            


addPP()
validatePP()
checkEntries()

print(validatePP())
