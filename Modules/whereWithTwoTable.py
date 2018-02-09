import sys
from databasefile import *
from cartesianProduct import *
from printResult import *
from collections import OrderedDict



def greaterThan(comp1,comp2):
    return comp1>comp2

def greaterThanEqual(comp1,comp2):
    return comp1>=comp2

def lessThanEqual(comp1,comp2):
    return comp1<=comp2

def lessThan(comp1,comp2):
    return comp1<comp2

def equal(comp1,comp2):
    return comp1==comp2

def notEqual(comp1,comp2):
    return comp1!=comp2

def selectAllWithOneCondition(tableNames,query,afterWhere,betFromAndWhere,betSelectAndFrom):
    try:
        productList = cartesianProduct(tableNames)
        allKeys = allTable[tableNames[0]].keys() + allTable[tableNames[1]].keys()

        columns = [afterWhere[0]]

        for cols in columns:
            if cols not in allKeys:
                sys.exit("ERROR: '"+cols.upper()+"' DOES NOT EXIST IN ANY TABLE")

        for key in columns:
            if allKeys.count(key) !=1:
                sys.exit("ERROR: COLUMN '"+key.upper()+"' IN FIELD LIST IS AMBIGIOUS")
        # if len(allKeys) != len(set(allKeys)):
        #     sys.exit("ERROR: AMBIGIOUS COLUMN IN TABLES")

        columnsIndex = []
        for cols in columns:
            columnsIndex.append(allKeys.index(cols))

        resultRows = []
        for row in productList:
            comp1 = False
            if afterWhere[1] == ">":
                comp1 = greaterThan(row[columnsIndex[0]],int(afterWhere[2]))
            elif afterWhere[1] == "<":
                comp1 = lessThan(row[columnsIndex[0]],int(afterWhere[2]))
            elif afterWhere[1] == "=":
                comp1 = equal(row[columnsIndex[0]],int(afterWhere[2]))
            elif afterWhere[1] == "@":
                comp1 = lessThanEqual(row[columnsIndex[0]],int(afterWhere[2]))
            elif afterWhere[1] == "#":
                comp1 = greaterThanEqual(row[columnsIndex[0]],int(afterWhere[2]))
            elif afterWhere[1] == "$":
                comp1 = notEqual(row[columnsIndex[0]],int(afterWhere[2]))

            if comp1:
                resultRows.append(row)

        allKeys = allTable[tableNames[0]].keys() + allTable[tableNames[1]].keys()
        for table in tableNames:
            for key in allTable[table].keys():
                allKeys[allKeys.index(key)] = table+"."+key
        # for key in allKeys:
        #     allKeys[allKeys.index(key)] = key.upper()
        printResult(allKeys,resultRows)
    except Exception as e:
        print e
        sys.exit("ERROR: CHECK QUERY SYNTAX")


def selectAllWithTwoCondition(tableNames,query,afterWhere,betFromAndWhere,betSelectAndFrom):
    try:
        productList = cartesianProduct(tableNames)
        allKeys = allTable[tableNames[0]].keys() + allTable[tableNames[1]].keys()
        # if len(allKeys) != len(set(allKeys)):
        #     sys.exit("ERROR: AMBIGIOUS COLUMN IN TABLES")
        columns = [afterWhere[0],afterWhere[4]]

        for cols in columns:
            if cols not in allKeys:
                sys.exit("ERROR: '"+cols.upper()+"' DOES NOT EXIST IN ANY TABLE")

        for key in columns:
            if allKeys.count(key) !=1:
                sys.exit("ERROR: COLUMN '"+key.upper()+"' IN FIELD LIST IS AMBIGIOUS")


        columnsIndex = []
        for cols in columns:
            columnsIndex.append(allKeys.index(cols))

        resultRows = []
        for row in productList:
            comp1 = False
            comp2 = False
            if afterWhere[1] == ">":
                comp1 = greaterThan(row[columnsIndex[0]],int(afterWhere[2]))
            elif afterWhere[1] == "<":
                comp1 = lessThan(row[columnsIndex[0]],int(afterWhere[2]))
            elif afterWhere[1] == "=":
                comp1 = equal(row[columnsIndex[0]],int(afterWhere[2]))
            elif afterWhere[1] == "@":
                comp1 = lessThanEqual(row[columnsIndex[0]],int(afterWhere[2]))
            elif afterWhere[1] == "#":
                comp1 = greaterThanEqual(row[columnsIndex[0]],int(afterWhere[2]))
            elif afterWhere[1] == "$":
                comp1 = notEqual(row[columnsIndex[0]],int(afterWhere[2]))


            if afterWhere[5] == ">":
                comp2 = greaterThan(row[columnsIndex[1]],int(afterWhere[6]))
            elif afterWhere[5] == "<":
                comp2 = lessThan(row[columnsIndex[1]],int(afterWhere[6]))
            elif afterWhere[5] == "=":
                comp2 = equal(row[columnsIndex[1]],int(afterWhere[6]))
            elif afterWhere[5] == "@":
                comp2 = lessThanEqual(row[columnsIndex[1]],int(afterWhere[6]))
            elif afterWhere[5] == "#":
                comp2 = greaterThanEqual(row[columnsIndex[1]],int(afterWhere[6]))
            elif afterWhere[5] == "$":
                comp2 = notEqual(row[columnsIndex[1]],int(afterWhere[6]))

            if afterWhere[3] == "or":
                if comp1 or comp2 :
                    resultRows.append(row)
            if afterWhere[3] == "and":
                if comp1 and comp2 :
                    resultRows.append(row)
        for table in tableNames:
            for key in allTable[table].keys():
                allKeys[allKeys.index(key)] = table+"."+key
        # for key in allKeys:
        #     allKeys[allKeys.index(key)] = key.upper()
        printResult(allKeys,resultRows)
    except Exception as e:
        print e
        sys.exit("ERROR: CHECK QUERY SYNTAX")


def selectColumnWithOneCondition(tableNames,query,afterWhere,betFromAndWhere,betSelectAndFrom):
    try:
        productList = cartesianProduct(tableNames)
        tableCols = ''.join(betSelectAndFrom).split(",")
        allKeys = allTable[tableNames[0]].keys() + allTable[tableNames[1]].keys()

        if "." in betSelectAndFrom:
            for col in tableCols:
                tableCols[tableCols.index(col)]  = col.split(".")[1]

        for key in tableCols:
            if allKeys.count(key) !=1:
                sys.exit("ERROR: COLUMN '"+key.upper()+"' IN FIELD LIST IS AMBIGIOUS")

        for col in tableCols:
            if col not in allKeys:
                sys.exit("ERROR : '"+col.upper()+"' NOT PRESENT IN ANY TABLE")

        columns = [afterWhere[0]]
        for cols in columns:
            if cols not in allKeys:
                sys.exit("ERROR: '"+cols.upper()+"' DOES NOT EXIST IN ANY TABLE")
        columnsIndex = []
        for cols in columns:
            columnsIndex.append(allKeys.index(cols))

        resultRows = []
        selectColsIndex = []
        for cols in tableCols:
            selectColsIndex.append(allKeys.index(cols))


        for row in productList:
            tempRow=[]
            comp1 = False
            comp2 = False
            if afterWhere[1] == ">":
                comp1 = greaterThan(row[columnsIndex[0]],int(afterWhere[2]))
            elif afterWhere[1] == "<":
                comp1 = lessThan(row[columnsIndex[0]],int(afterWhere[2]))
            elif afterWhere[1] == "=":
                comp1 = equal(row[columnsIndex[0]],int(afterWhere[2]))
            elif afterWhere[1] == "@":
                comp1 = lessThanEqual(row[columnsIndex[0]],int(afterWhere[2]))
            elif afterWhere[1] == "#":
                comp1 = greaterThanEqual(row[columnsIndex[0]],int(afterWhere[2]))
            elif afterWhere[1] == "$":
                comp1 = notEqual(row[columnsIndex[0]],int(afterWhere[2]))

            if comp1  :
                for index in selectColsIndex:
                    tempRow.append(row[index])
                resultRows.append(tempRow)
        for table in tableNames:
            for key in allTable[table].keys():
                if key in tableCols:
                    tableCols[tableCols.index(key)] = table+"."+key
        # for key in tableCols:
        #     tableCols[tableCols.index(key)] = key.upper()
        printResult(tableCols,resultRows)
    except exception as e:
        print e
        sys.exit("ERROR: PLEASE CHECK QUERY SYNTAX")


def selectColumnWithTwoCondition(tableNames,query,afterWhere,betFromAndWhere,betSelectAndFrom):
    try:
        productList = cartesianProduct(tableNames)
        tableCols = ''.join(betSelectAndFrom).split(",")
        allKeys = allTable[tableNames[0]].keys() + allTable[tableNames[1]].keys()

        if "." in betSelectAndFrom:
            for col in tableCols:
                tableCols[tableCols.index(col)]  = col.split(".")[1]

        for key in tableCols:
            if allKeys.count(key) !=1:
                sys.exit("ERROR: COLUMN '"+key.upper()+"' IN FIELD LIST IS AMBIGIOUS")

        for col in tableCols:
            if col not in allKeys:
                sys.exit("ERROR : '"+col.upper()+"' NOT PRESENT IN ANY TABLE")



        columns = [afterWhere[0],afterWhere[4]]
        for cols in columns:
            if cols not in allKeys:
                sys.exit("ERROR: '"+cols.upper()+"' DOES NOT EXIST IN ANY TABLE")
        columnsIndex = []
        for cols in columns:
            columnsIndex.append(allKeys.index(cols))

        resultRows = []
        selectColsIndex = []
        for cols in tableCols:
            selectColsIndex.append(allKeys.index(cols))


        for row in productList:
            tempRow=[]
            comp1 = False
            comp2 = False
            if afterWhere[1] == ">":
                comp1 = greaterThan(row[columnsIndex[0]],int(afterWhere[2]))
            elif afterWhere[1] == "<":
                comp1 = lessThan(row[columnsIndex[0]],int(afterWhere[2]))
            elif afterWhere[1] == "=":
                comp1 = equal(row[columnsIndex[0]],int(afterWhere[2]))
            elif afterWhere[1] == "@":
                comp1 = lessThanEqual(row[columnsIndex[0]],int(afterWhere[2]))
            elif afterWhere[1] == "#":
                comp1 = greaterThanEqual(row[columnsIndex[0]],int(afterWhere[2]))
            elif afterWhere[1] == "$":
                comp1 = notEqual(row[columnsIndex[0]],int(afterWhere[2]))


            if afterWhere[5] == ">":
                comp2 = greaterThan(row[columnsIndex[1]],int(afterWhere[6]))
            elif afterWhere[5] == "<":
                comp2 = lessThan(row[columnsIndex[1]],int(afterWhere[6]))
            elif afterWhere[5] == "=":
                comp2 = equal(row[columnsIndex[1]],int(afterWhere[6]))
            elif afterWhere[5] == "@":
                comp2 = lessThanEqual(row[columnsIndex[1]],int(afterWhere[6]))
            elif afterWhere[5] == "#":
                comp2 = greaterThanEqual(row[columnsIndex[1]],int(afterWhere[6]))
            elif afterWhere[5] == "$":
                comp2 = notEqual(row[columnsIndex[1]],int(afterWhere[6]))


            if afterWhere[3] == "or":
                if comp1 or comp2 :
                    for index in selectColsIndex:
                        tempRow.append(row[index])
                    resultRows.append(tempRow)
            if afterWhere[3] == "and":
                if comp1 and comp2 :
                    for index in selectColsIndex:
                        tempRow.append(row[index])
                    resultRows.append(tempRow)
        for table in tableNames:
            for key in allTable[table].keys():
                if key in tableCols:
                    tableCols[tableCols.index(key)] = table+"."+key
        # for key in tableCols:
        #     tableCols[tableCols.index(key)] = key.upper()
        printResult(tableCols,resultRows)
    except Exception as e:
        print e
        sys.exit("ERROR: PLEASE CHECK QUERY SYNTAX")


def selectAllWithDotAfterWhere(tableNames,query,afterWhere,betFromAndWhere,betSelectAndFrom):
    try:
        productList = cartesianProduct(tableNames)
        allKeys = allTable[tableNames[0]].keys() + allTable[tableNames[1]].keys()
        if len(afterWhere)==7:
            whereTables = [afterWhere[0]]+ [afterWhere[4]]
            whereCols = [afterWhere[2]]+ [afterWhere[6]]
            columns = [afterWhere[2],afterWhere[6]]
        elif len(afterWhere)==15:
            whereTables = [afterWhere[0]]+ [afterWhere[4]] + [afterWhere[8]]+ [afterWhere[12]]
            whereCols = [afterWhere[2]]+ [afterWhere[6]] + [afterWhere[10]] + [afterWhere[14]]
            columns = [afterWhere[2],afterWhere[6],afterWhere[10],afterWhere[14]]
        for tName in whereTables:
            if tName not in tableNames:
                sys.exit("ERROR: '"+tName.upper()+"' DOES NOT EXIST IN ANY TABLES")
        for tCol in whereCols:
            if tCol not in allKeys:
                sys.exit("ERROR: '"+tCol.upper()+"' DOES NOT EXIST IN ANY TABLES")





        columnsIndex = []

        resultRows = []

        try:
            if len(afterWhere)==7:
                if tableNames.index(whereTables[0]) == 1:
                    columnsIndex.append(allTable[whereTables[0]].keys().index(whereCols[0])+len(allTable[tableNames[0]].keys()))
                else:
                    columnsIndex.append(allTable[whereTables[0]].keys().index(whereCols[0]))

                if tableNames.index(whereTables[1]) == 1:
                    columnsIndex.append(allTable[whereTables[1]].keys().index(whereCols[1])+len(allTable[tableNames[0]].keys()))
                else:
                    columnsIndex.append(allTable[whereTables[1]].keys().index(whereCols[1]))
            elif len(afterWhere)==15:
                if tableNames.index(whereTables[0]) == 1:
                    columnsIndex.append(allTable[whereTables[0]].keys().index(whereCols[0])+len(allTable[tableNames[0]].keys()))
                else:
                    columnsIndex.append(allTable[whereTables[0]].keys().index(whereCols[0]))
                if tableNames.index(whereTables[1]) == 1:
                    columnsIndex.append(allTable[whereTables[1]].keys().index(whereCols[1])+len(allTable[tableNames[0]].keys()))
                else:
                    columnsIndex.append(allTable[whereTables[1]].keys().index(whereCols[1]))

                if tableNames.index(whereTables[2]) == 1:
                    columnsIndex.append(allTable[whereTables[2]].keys().index(whereCols[2])+len(allTable[tableNames[0]].keys()))
                else:
                    columnsIndex.append(allTable[whereTables[2]].keys().index(whereCols[2]))
                if tableNames.index(whereTables[3]) == 1:
                    columnsIndex.append(allTable[whereTables[3]].keys().index(whereCols[3])+len(allTable[tableNames[0]].keys()))
                else:
                    columnsIndex.append(allTable[whereTables[3]].keys().index(whereCols[3]))

        except:
            sys.exit("ERROR: INVALID COLUMN COMBINATION")

        if len(afterWhere)==7:
            for row in productList:
                if afterWhere[3]=="=":
                    if row[columnsIndex[0]] == row[columnsIndex[1]] :
                        resultRows.append(row)
                if afterWhere[3]=="<":
                    if row[columnsIndex[0]] < row[columnsIndex[1]] :
                        resultRows.append(row)
                if afterWhere[3]==">":
                    if row[columnsIndex[0]] > row[columnsIndex[1]] :
                        resultRows.append(row)
                if afterWhere[3]=="@":
                    if row[columnsIndex[0]] <= row[columnsIndex[1]] :
                        resultRows.append(row)
                if afterWhere[3]=="#":
                    if row[columnsIndex[0]] >= row[columnsIndex[1]] :
                        resultRows.append(row)



            table1Keys = allTable[tableNames[0]].keys()
            for keys in table1Keys:
                table1Keys[table1Keys.index(keys)] = tableNames[0]+"."+keys
            table2Keys = allTable[tableNames[1]].keys()
            for keys in table2Keys:
                table2Keys[table2Keys.index(keys)] = tableNames[1]+"."+keys
            allcols = table1Keys + table2Keys

            # for table in tableNames:
            #     for key in allTable[table].keys():
            #         if key in tableCols:
            #             allcols[allcols.index(key)] = table+"."+key
            # for key in allcols:
            #     allcols[allcols.index(key)] = key.upper()

            # print "Hello"
            commonColIndex = allKeys.index(afterWhere[2])
            if afterWhere[3]=="=":
                for row in resultRows:
                    del row[commonColIndex]
                del allcols[commonColIndex]
            printResult(allcols,resultRows)

        elif len(afterWhere)==15:
            for row in productList:
                comp1 = False
                comp2 = False
                if afterWhere[3] == ">":
                    comp1 = greaterThan(row[columnsIndex[0]], row[columnsIndex[1]])
                elif afterWhere[3] == "<":
                    comp1 = lessThan(row[columnsIndex[0]], row[columnsIndex[1]])
                elif afterWhere[3] == "=":
                    comp1 = equal(row[columnsIndex[0]], row[columnsIndex[1]])
                elif afterWhere[3] == "@":
                    comp1 = lessThanEqual(row[columnsIndex[0]], row[columnsIndex[1]])
                elif afterWhere[3] == "#":
                    comp1 = greaterThanEqual(row[columnsIndex[0]], row[columnsIndex[1]])
                elif afterWhere[3] == "$":
                    comp1 = notEqual(row[columnsIndex[0]], row[columnsIndex[1]])


                if afterWhere[11] == ">":
                    comp2 = greaterThan(row[columnsIndex[2]], row[columnsIndex[3]])
                elif afterWhere[11] == "<":
                    comp2 = lessThan(row[columnsIndex[2]], row[columnsIndex[3]])
                elif afterWhere[11] == "=":
                    comp2 = equal(row[columnsIndex[2]], row[columnsIndex[3]])
                elif afterWhere[11] == "@":
                    comp2 = lessThanEqual(row[columnsIndex[2]], row[columnsIndex[3]])
                elif afterWhere[11] == "#":
                    comp2 = greaterThanEqua(row[columnsIndex[2]], row[columnsIndex[3]])
                elif afterWhere[11] == "$":
                    comp2 = notEqual(row[columnsIndex[2]], row[columnsIndex[3]])

                if afterWhere[7] == "or":
                    if comp1 or comp2:
                        resultRows.append(row)
                elif afterWhere[7] == "and":
                    if comp1 and comp2:
                        resultRows.append(row)



            table1Keys = allTable[tableNames[0]].keys()
            for keys in table1Keys:
                table1Keys[table1Keys.index(keys)] = tableNames[0]+"."+keys
            table2Keys = allTable[tableNames[1]].keys()
            for keys in table2Keys:
                table2Keys[table2Keys.index(keys)] = tableNames[1]+"."+keys
            allcols = table1Keys + table2Keys
            # for key in allcols:
            #     allcols[allcols.index(key)] = key.upper()
            printResult(allcols,resultRows)
        else:
            sys.exit("ERROR: PLEASE CHECK QUERY SYNTAX")
    except Exception as e:
        print e
        sts.exit("ERROR: CHECK QUERY SYNTAX")




def selectColumnWithDotAfterWhere(tableNames,query,afterWhere,betFromAndWhere,betSelectAndFrom):
    try:
        productList = cartesianProduct(tableNames)
        tableCols = ''.join(betSelectAndFrom).split(",")
        allKeys = allTable[tableNames[0]].keys() + allTable[tableNames[1]].keys()




        if "." in betSelectAndFrom:
            for col in tableCols:
                tableCols[tableCols.index(col)]  = col.split(".")[1]

        for key in tableCols:
            if allKeys.count(key) !=1 and "." not in betSelectAndFrom :
                sys.exit("ERROR: COLUMN '"+key.upper()+"' IN FIELD LIST IS AMBIGIOUS")

        for col in tableCols:
            if col not in allKeys:
                sys.exit("ERROR : '"+col.upper()+"' NOT PRESENT IN ANY TABLE")

        selectColsIndex = []
        for cols in tableCols:
            selectColsIndex.append(allKeys.index(cols))

        columns = [afterWhere[2],afterWhere[6]]
        for cols in columns:
            if cols not in allKeys:
                sys.exit("ERROR: '"+cols.upper()+"' DOES NOT EXIST IN ANY TABLE")


        if len(afterWhere)==7:
            whereTables = [afterWhere[0]]+ [afterWhere[4]]
            whereCols = [afterWhere[2]]+ [afterWhere[6]]
            columns = [afterWhere[2],afterWhere[6]]
        elif len(afterWhere)==15:
            whereTables = [afterWhere[0]]+ [afterWhere[4]] + [afterWhere[8]]+ [afterWhere[12]]
            whereCols = [afterWhere[2]]+ [afterWhere[6]] + [afterWhere[10]] + [afterWhere[14]]
            columns = [afterWhere[2],afterWhere[6],afterWhere[10],afterWhere[14]]


        for tName in whereTables:
            if tName not in tableNames:
                sys.exit("ERROR: '"+tName.upper()+"' DOES NOT EXIST IN ANY TABLES")
        for tCol in whereCols:
            if tCol not in allKeys:
                sys.exit("ERROR: '"+tCol.upper()+"' DOES NOT EXIST IN ANY TABLES")

        columnsIndex = []

        resultRows = []
        try:
            if len(afterWhere)==7:
                if tableNames.index(whereTables[0]) == 1:
                    columnsIndex.append(allTable[whereTables[0]].keys().index(whereCols[0])+len(allTable[tableNames[0]].keys()))
                else:
                    columnsIndex.append(allTable[whereTables[0]].keys().index(whereCols[0]))

                if tableNames.index(whereTables[1]) == 1:
                    columnsIndex.append(allTable[whereTables[1]].keys().index(whereCols[1])+len(allTable[tableNames[0]].keys()))
                else:
                    columnsIndex.append(allTable[whereTables[1]].keys().index(whereCols[1]))
            elif len(afterWhere)==15:
                if tableNames.index(whereTables[0]) == 1:
                    columnsIndex.append(allTable[whereTables[0]].keys().index(whereCols[0])+len(allTable[tableNames[0]].keys()))
                else:
                    columnsIndex.append(allTable[whereTables[0]].keys().index(whereCols[0]))
                if tableNames.index(whereTables[1]) == 1:
                    columnsIndex.append(allTable[whereTables[1]].keys().index(whereCols[1])+len(allTable[tableNames[0]].keys()))
                else:
                    columnsIndex.append(allTable[whereTables[1]].keys().index(whereCols[1]))

                if tableNames.index(whereTables[2]) == 1:
                    columnsIndex.append(allTable[whereTables[2]].keys().index(whereCols[2])+len(allTable[tableNames[0]].keys()))
                else:
                    columnsIndex.append(allTable[whereTables[2]].keys().index(whereCols[2]))
                if tableNames.index(whereTables[3]) == 1:
                    columnsIndex.append(allTable[whereTables[3]].keys().index(whereCols[3])+len(allTable[tableNames[0]].keys()))
                else:
                    columnsIndex.append(allTable[whereTables[3]].keys().index(whereCols[3]))

        except:
            sys.exit("ERROR: INVALID COLUMN COMBINATION")








        if len(afterWhere)==7:
            for row in productList:
                tempRow = []
                if afterWhere[3]=="=":
                    if row[columnsIndex[0]] == row[columnsIndex[1]] :
                        for index in selectColsIndex:
                            tempRow.append(row[index])
                        resultRows.append(tempRow)
                if afterWhere[3]=="<":
                    if row[columnsIndex[0]] < row[columnsIndex[1]] :
                        for index in selectColsIndex:
                            tempRow.append(row[index])
                        resultRows.append(tempRow)
                if afterWhere[3]==">":
                    if row[columnsIndex[0]] > row[columnsIndex[1]] :
                        for index in selectColsIndex:
                            tempRow.append(row[index])
                        resultRows.append(tempRow)
                if afterWhere[3]=="@":
                    if row[columnsIndex[0]] <= row[columnsIndex[1]] :
                        for index in selectColsIndex:
                            tempRow.append(row[index])
                        resultRows.append(tempRow)
                if afterWhere[3]=="#":
                    if row[columnsIndex[0]] >= row[columnsIndex[1]] :
                        for index in selectColsIndex:
                            tempRow.append(row[index])
                        resultRows.append(tempRow)

            # for key in tableCols:
            #     tableCols[tableCols.index(key)] = key.upper()
            for table in tableNames:
                for key in allTable[table].keys():
                    if key in tableCols:
                        tableCols[tableCols.index(key)] = table+"."+key
            printResult(tableCols,resultRows)
        elif len(afterWhere)==15:
            for row in productList:
                comp1 = False
                comp2 = False
                tempRow = []
                if afterWhere[3] == ">":
                    comp1 = greaterThan(row[columnsIndex[0]], row[columnsIndex[1]])
                elif afterWhere[3] == "<":
                    comp1 = lessThan(row[columnsIndex[0]], row[columnsIndex[1]])
                elif afterWhere[3] == "=":
                    comp1 = equal(row[columnsIndex[0]], row[columnsIndex[1]])
                elif afterWhere[3] == "@":
                    comp1 = lessThanEqual(row[columnsIndex[0]], row[columnsIndex[1]])
                elif afterWhere[3] == "#":
                    comp1 = greaterThanEqual(row[columnsIndex[0]], row[columnsIndex[1]])
                elif afterWhere[3] == "$":
                    comp1 = notEqual(row[columnsIndex[0]], row[columnsIndex[1]])


                if afterWhere[11] == ">":
                    comp2 = greaterThan(row[columnsIndex[2]], row[columnsIndex[3]])
                elif afterWhere[11] == "<":
                    comp2 = lessThan(row[columnsIndex[2]], row[columnsIndex[3]])
                elif afterWhere[11] == "=":
                    comp2 = equal(row[columnsIndex[2]], row[columnsIndex[3]])
                elif afterWhere[11] == "@":
                    comp2 = lessThanEqual(row[columnsIndex[2]], row[columnsIndex[3]])
                elif afterWhere[11] == "#":
                    comp2 = greaterThanEqua(row[columnsIndex[2]], row[columnsIndex[3]])
                elif afterWhere[11] == "$":
                    comp2 = notEqual(row[columnsIndex[2]], row[columnsIndex[3]])

                if afterWhere[7] == "or":
                    if comp1 or comp2:
                        for index in selectColsIndex:
                            tempRow.append(row[index])
                        resultRows.append(tempRow)
                elif afterWhere[7] == "and":
                    if comp1 and comp2:
                        for index in selectColsIndex:
                            tempRow.append(row[index])
                        resultRows.append(tempRow)
            for table in tableNames:
                for key in allTable[table].keys():
                    if key in tableCols:
                        tableCols[tableCols.index(key)] = table+"."+key
            # for key in tableCols:
            #     tableCols[tableCols.index(key)] = key.upper()
            printResult(tableCols,resultRows)
        else:
            sys.exit("ERROR: PLEASE CHECK QUERY SYNTAX")
    except Exception as e:
        print e
        sys.exit("ERROR: PLEASE CHECK QUERY SYNTAX")



def whereWithTwoTable(tableNames,query,afterWhere,betFromAndWhere,betSelectAndFrom):
    try:
        if "." not in afterWhere:

            if query[1] == "*":
                if len(afterWhere) == 3:
                    selectAllWithOneCondition(tableNames,query,afterWhere,betFromAndWhere,betSelectAndFrom)
                elif len(afterWhere) == 7:
                    selectAllWithTwoCondition(tableNames,query,afterWhere,betFromAndWhere,betSelectAndFrom)
                else:
                    sys.exit("ERROR: CHECK QUERY SYNTAX OR UNSUPPORTED QUERY")
            else:
                if len(afterWhere) == 3:
                    selectColumnWithOneCondition(tableNames,query,afterWhere,betFromAndWhere,betSelectAndFrom)
                elif len(afterWhere) == 7:
                    selectColumnWithTwoCondition(tableNames,query,afterWhere,betFromAndWhere,betSelectAndFrom)
                else:
                    sys.exit("ERROR: CHECK QUERY SYNTAX OR UNSUPPORTED QUERY")


        elif "." in afterWhere:
            if query[1] == "*":
                selectAllWithDotAfterWhere(tableNames,query,afterWhere,betFromAndWhere,betSelectAndFrom)
            else:
                selectColumnWithDotAfterWhere(tableNames,query,afterWhere,betFromAndWhere,betSelectAndFrom)
        else:
            sys.exit("ERROR: PLEASE CHECK QUERY SYNTAX")
    except Exception as e:
        print e
        sys.exit("ERROR PLEASE CHECK QUERY SYNTAX")
