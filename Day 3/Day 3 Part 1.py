linesize = 0
trees = 0

with open("Map", "r") as f:
    lines = f.readlines()
    # reads all lines into a list of strings


    for LineNumber in range(0, len(f.readlines())):
        while LineNumber <= len(f.readlines()):
            for j in range(0, 2):
                if lines[LineNumber][j] == "#":
                    # if there is a hash in LineNumber position j, then tree count needs to be updated
                    trees += 1
                    # if character is a hash, then add one to the count of trees and continue
                    LineNumber += 1
                    # proceed to next line of the file but need to make position starting position [j] again to /
                    # to continue the count
                    break


