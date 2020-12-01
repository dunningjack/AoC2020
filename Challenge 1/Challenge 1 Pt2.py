expenses = []
length = len(expenses)

file = "expenses"

with open(file, 'r') as f:
    for line in f:
        toWrite = line.rstrip("\n")
        expenses.append(int(toWrite))


for i in range(0, len(expenses)):
    remaining = 2020 - expenses[i]
    # finds remainder

    for k in range(i+1, len(expenses)):
        secondremain = remaining - expenses[k]
        # finds what is left after looping through again and removing the 2nd number needed

        if secondremain in expenses:
            print((expenses[i], expenses[k], secondremain), (remaining * expenses[i] * secondremain))
            # should find the final number needed
