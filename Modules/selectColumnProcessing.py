import sys
from databasefile import *
from cartesianProduct import *
from printResult import *
import copy

def selectColumnProcessing(query):
    try:
        fromIndex =  query.index("from")
        tableNames = query[fromIndex + 1 : ]
        tableNames = ''.join(tableNames)
        tableNames = tableNames.rstrip(";")
        tableNames = tableNames.split(",")
        # print tableNames
        for tableName in tableNames:
            if tableName not in allTable.keys():
                sys.exit("ERROR: TABLE '"+ tableName +"' NOT EXIST IN DATABASE!!")

        columnNames = query[1:fromIndex]
        columnNames = ''.join(columnNames)
        columnNames = columnNames.split(",")


        if len(tableNames) == 1:
            rowsInColumn = []
            TableCols = allTable[tableNames[0]].keys()
            for col in columnNames:
                if col not in TableCols:
                    sys.exit("ERROR: COLUMN '"+col.upper() +"' DOES NOT EXIST IN '"+ tableNames[0]+"'")
            rows = 0
            indexofcols = []
            allrows = []
            for col in columnNames:
                indexofcols.append(allTable[tableNames[0]].keys().index(col))
            while(rows < len(allTable[tableNames[0]].values()[0])):
                cols = 0
                colRows = []
                while (cols < len(columnNames)):
                    colRows.append(allTable[tableNames[0]].values()[indexofcols[cols]][rows])
                    cols = cols + 1
                rows = rows + 1
                allrows.append(colRows)
            for cols in columnNames:
                columnNames[columnNames.index(cols)] = tableNames[0]+"."+cols
            printResult(columnNames,allrows)
        else:
            # print columnNames
            tempCols = copy.copy(columnNames)
            tableCols = OrderedDict()
            for tName in tableNames:
                tableCols[tName] = []
            allcols = []
            cartProductCols = OrderedDict()
            for col in columnNames:
                flag = 0
                for tName in tableNames:
                    if col in allTable[tName].keys():
                        tableCols[tName].append(col)
                        # print allTable[tName].keys().index(col)
                        cartProductCols[col]=allTable[tName].values()[allTable[tName].keys().index(col)]
                        flag = 1
                if flag == 1:
                    tempCols.remove(col)
            for cols in tableCols:
                for col in tableCols[cols]:
                    allcols.append(col)

            for col in columnNames:
                if col not in allcols:
                    sys.exit("ERROR: '"+col.upper()+"' COLUMN DOES NOT EXIST IN ANY TABLE")

            uniqueCol = []
            duplicate = []
            for col in allcols:
                if col not in uniqueCol:
                    uniqueCol.append(col)
                else:
                    duplicate.append(col)

            resultCartProduct = []

            if len(uniqueCol)==1 and len(duplicate) == 0:
                extraTable = []
                for cols in tableCols:
                    if uniqueCol[0] not in  tableCols[cols]:
                        extraTable.append(cols)
                for value1 in range(0, len(cartProductCols[uniqueCol[0]])):
                    for value2 in range(0,len(extraTable)):
                        for value3 in range(0,len(allTable[extraTable[0]].values()[0])):
                            rowsInCartProduct = []
                            rowsInCartProduct.append(cartProductCols[uniqueCol[0]][value1])
                            resultCartProduct.append(rowsInCartProduct)
                for col in uniqueCol:
                    if col in tableNames[0]:
                        uniqueCol = tableNames[0]+"."+col
                    else:
                        uniqueCol = tableNames[1]+"."+col

                printResult([uniqueCol],resultCartProduct)
                sys.exit()
            if len(duplicate) == 0:
                try:
                    # print uniqueCol
                    if len(tempCols) == 0:
                        for value1 in range(0, len(cartProductCols[uniqueCol[0]])):
                            for value2 in range(0, len(cartProductCols[uniqueCol[1]])):
                                rowsInCartProduct = []
                                rowsInCartProduct.append(cartProductCols[uniqueCol[0]][value1])
                                rowsInCartProduct.append(cartProductCols[uniqueCol[1]][value2])
                                resultCartProduct.append(rowsInCartProduct)
                        for col in uniqueCol:
                            if col in tableNames[0]:
                                uniqueCol[uniqueCol.index(col)] = tableNames[0]+"."+col
                            else:
                                uniqueCol[uniqueCol.index(col)] = tableNames[1]+"."+col
                        printResult(uniqueCol,resultCartProduct)
                    else:
                        sys.exit("ERROR: COLUMN '"+ ''.join(tempCols).upper() +"' DOES NOT BELONG TO ANY TABLE")
                except:
                    sys.exit("ERROR: SUCH COMPLEX QUERY DOESN'T SUPPORTED IN CURRENT VERSION" )
            else:
                sys.exit("ERROR: COLUMN '"+ ''.join(duplicate).upper() +"' IN FIELD LIST IS AMBIGUOUS IN TABLES")
    except Exception as e:
        print e
        sys.exit("ERROR: PLEASE CHECK QUERY SYNTAX")
