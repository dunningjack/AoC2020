with open("Seats", 'r') as f:
    seatlist = f.readlines()

    def rowfinder():
        seatrow = []
        for i in range(0, len(seatlist)):
            rows = []
            rows.extend(range(0, 127))
            k = 127
            for j in range(0, 9):
                if seatlist[i][j] == "F":
                    del rows[63:127]
                else:
                    del rows[0:63]
                seatrow.append(rows[j])
        return seatrow


    def columnfinder():
        seatcolumn = []
        for i in range(0, len(seatlist)):
            columns = []
            columns.extend(range(0,7))
            for j in range(0, 9):
                if seatlist[i][j] == "L":
                    del columns[3:7]
                else:
                    del columns[0:3]
                seatcolumn.append(columns[j])
        return seatcolumn

seatrow = rowfinder()
seatcolumn = columnfinder()


rowfinder()
columnfinder()
for i in range(0, len(rowfinder())):
    print(seatrow[i], seatcolumn[i])