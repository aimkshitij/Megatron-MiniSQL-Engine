import sys
from databasefile import *


def cartesianProduct(tableNames):
    try:
        table1 = []
        table2 = []
        i=1
        for table in tableNames:
            rows = 0
            while(rows < len(allTable[table].values()[0])):
                cols = 0
                rowlist = []
                while (cols < len(allTable[table].keys())):
                    rowlist.append(allTable[table].values()[cols][rows])
                    cols = cols + 1
                rows = rows + 1
                if i==1:
                    table1.append(rowlist)
                else:
                    table2.append(rowlist)
            i=i+1
        newTable = []
        for rowT1 in table1:
            rowNewTable = []
            for rowT2 in table2:
                newTable.append(rowT1 + rowT2)
        table1Keys = allTable[tableNames[0]].keys()
        for keys in table1Keys:
            table1Keys[table1Keys.index(keys)] = keys +  "."+tableNames[0]
        table2Keys = allTable[tableNames[1]].keys()
        for keys in table2Keys:
            table2Keys[table2Keys.index(keys)] = keys +  "."+tableNames[1]
        allcols = table1Keys + table2Keys
        return newTable

    except Exception as e:
        print e
        sys.exit("ERROR: DURING CARTESIAN PRODUCT")
