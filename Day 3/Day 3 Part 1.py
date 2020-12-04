linesize = 0
treecount = 0
x = 0
y = 2

with open("Map", "r") as f:
    lines = f.readlines()
    # reads all lines into a list of strings

    for i in range(0, len(lines)):
        for j in range(0, len(lines[i])):
            if j % 3 == 1:
                if lines[i][j] == "#":
                    treecount += 1
            j = 0


print(treecount)
