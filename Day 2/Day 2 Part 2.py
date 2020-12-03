file = "passwords"
total = 0
valid = 0

with open(file, 'r') as f:

    for line in f:
        parts = line.split(" ")
        bounds = parts[0].split("-")
        LB = int(bounds[0])
        UB = int(bounds[1])
        first = LB - 1
        second = UB - 1
        search = parts[1].strip(":")


        # for j in range(0, len(parts)):
            # if parts[2][j] == search:
                # count += 1
        pword = parts[2]
        count = pword.count(search)

        if count >= int(LB) and count <= int(UB):
            total += 1

        if (pword[first] == search) is not (pword[second] == search):
            valid += 1

print(valid)
