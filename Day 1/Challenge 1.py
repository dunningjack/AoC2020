expenses = []
length = len(expenses)

file = "expenses"

with open(file, 'r') as f:
    for line in f:
        toWrite = line.rstrip("\n")
        expenses.append(int(toWrite))


for i in range(0, len(expenses)):
    remaining = 2020 - expenses[i]

    if remaining in expenses:
        print((remaining, expenses[i]), (remaining * expenses[i]))
