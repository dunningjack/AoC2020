with open("Seats", 'r') as f:
    seatlist = f.readlines()

    def rowfinder():
        rows = 128
        seatrow = []
        for i in range(0, len(seatlist)):
            for j in range(0, 9):
                if seatlist[i][j] == "F":
                    rows / 2
                else:
                    rows = rows - (rows/2)
            seatrow.append(rows)
        return seatrow


    def columnfinder():
        columns = 8
        seatcolumn = []
        for i in range(0, len(seatlist)):
            for j in range(0, 9):
                if seatlist[i][j] == "L":
                    columns / 2
            else:
                columns = columns - (columns / 2)
            seatcolumn.append(columns)
        return seatcolumn

rowfinder()
columnfinder()
print(rowfinder(), columnfinder())