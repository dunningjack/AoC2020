with open("Seats", 'r') as f:
    lines = f.readlines()
    seatlist = []
    for i in range(0, len(lines)):
        seatlist.append(lines[i].strip())


    def rowfinder():
        seatrow = []
        for i in range(0, len(seatlist)):
            rows = []
            rows.extend(range(0, 127))
            # fills 128 indices with number
            k = int(128)
            for j in range(0, 6):
                if seatlist[i][j] == "F":
                    LB = int(k / 2)
                    UB = k
                    del rows[LB:UB]
                    rowlen = len(rows)
                    pos = rows[rowlen - 1]
                else:
                    LB = int(k / 2)
                    UB = k
                    del rows[0:LB]
                    rowlen = len(rows)
                    pos = rows[rowlen - 1]
                k = rowlen
            seatrow.append(pos)
        return seatrow


    def columnfinder():
        seatcolumn = []
        for i in range(0, len(seatlist)):
            columns = []
            columns.extend(range(0, 7))
            k = int(6)
            for j in range(7, 9):
                if seatlist[i][j] == "L":
                    LB = int(k / 2)
                    UB = k
                    del columns[LB:UB]
                    rowlen = len(columns)
                    pos = columns[rowlen - 1]
                else:
                    LB = int((k / 2) - 1)
                    UB = k
                    del columns[0:LB]
                    rowlen = len(columns)
                    pos = columns[rowlen - 1]
                k = rowlen
            seatcolumn.append(pos)
        return seatcolumn


    def seatIdent():
        seatID = []
        for i in range(0, len(seatrow)):
            row = seatrow[i] * 8
            col = seatcolumn[i]
            ID = row + col
            seatID.append(ID)
        return seatID


    seatrow = rowfinder()
    seatcolumn = columnfinder()
    seatID = seatIdent()

    rowfinder()
    columnfinder()
    seatIdent()


def sorter():
    seatID.sort(reverse=True)
    return seatID

print(sorter())
