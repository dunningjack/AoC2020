file = "passwords"

with open(file, 'r') as f:

    for line in f:
        parts = line.split(" ")

    for i in range(0, len(parts)):
        bounds = parts[0].split("-")
        LB = bounds[0]
        UB = bounds[1]
        search = parts[1].strip(":")

        count = 0
        total = 0

        # for j in range(0, len(parts)):
            # if parts[2][j] == search:
                # count += 1
        count = parts[2].count(search)

        if count > int(LB) and count < int(UB):
            total += 1
        print(total)
