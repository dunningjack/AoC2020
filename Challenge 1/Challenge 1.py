expenses = []
length = len(expenses)

file = "expenses"

with open(file, 'r') as f:
    for line in f:
        toWrite = line.rstrip("\n")
        expenses.append(int(toWrite))


for i in range(1, length):
    for k in range(0, length):
        if expenses[k] + expenses[i] == 2020:
            print(expenses[i], " + ", expenses[k], " = 2020")

