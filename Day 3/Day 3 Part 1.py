linesize = 0
trees = 0

with open("Map", "r") as f:
    lines = f.readlines()
    # reads all lines into a list of strings

    for i in range(0, len(lines)):
        for char in lines[i]:
            linesize += 1

        while i <= len(f.readlines()):
            for j in range(0, 2):
                if char[j] == "#":
                    trees += 1
                    break
                break
                i += 1
