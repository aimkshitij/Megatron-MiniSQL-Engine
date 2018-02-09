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

        tableData = OrderedDict()
        for cols in allTable[''.join(tableNames)]:
            tableData[cols]= allTable[''.join(tableNames)][cols]

            tableCols = ''.join(betSelectAndFrom).split(",")

        rows=0
        allrows=[]
        allcols=allTable[''.join(tableNames)].keys()
        while(rows < len(tableData.values()[0])):
            cols = 0
            rowlist = []
            if afterWhere[1] == "=":
                if tableData.values()[tableData.keys().index(afterWhere[0])][rows] ==  int(afterWhere[2]):
                    while (cols < len(tableData.keys())):
                        rowlist.append(tableData.values()[cols][rows])
                        cols = cols + 1
                    allrows.append(rowlist)
                rows = rows + 1
            if afterWhere[1] == "<":
                if tableData.values()[tableData.keys().index(afterWhere[0])][rows] <  int(afterWhere[2]):
                    while (cols < len(tableData.keys())):
                        rowlist.append(tableData.values()[cols][rows])
                        cols = cols + 1
                    allrows.append(rowlist)
                rows = rows + 1
            if afterWhere[1] == ">":
                if tableData.values()[tableData.keys().index(afterWhere[0])][rows] >  int(afterWhere[2]):
                    while (cols < len(tableData.keys())):
                        rowlist.append(tableData.values()[cols][rows])
                        cols = cols + 1
                    allrows.append(rowlist)
                rows = rows + 1
            if afterWhere[1] == "#":
                if tableData.values()[tableData.keys().index(afterWhere[0])][rows] >= int(afterWhere[2]):
                    while (cols < len(tableData.keys())):
                        rowlist.append(tableData.values()[cols][rows])
                        cols = cols + 1
                    allrows.append(rowlist)
                rows = rows + 1
            if afterWhere[1] == "@":
                if tableData.values()[tableData.keys().index(afterWhere[0])][rows] <=  int(afterWhere[2]):
                    while (cols < len(tableData.keys())):
                        rowlist.append(tableData.values()[cols][rows])
                        cols = cols + 1
                    allrows.append(rowlist)
                rows = rows + 1
            if afterWhere[1] == "$":
                if tableData.values()[tableData.keys().index(afterWhere[0])][rows] !=  int(afterWhere[2]):
                    while (cols < len(tableData.keys())):
                        rowlist.append(tableData.values()[cols][rows])
                        cols = cols + 1
                    allrows.append(rowlist)
                rows = rows + 1
        for cols in allcols:
            allcols[allcols.index(cols)] = tableNames[0]+"."+cols
        printResult(allcols,allrows)

    except Exception as e:
        print e
        sys.exit("ERROR CHECK QUERY SYNTAX")


def selectAllWithTwoCondition(tableNames,query,afterWhere,betFromAndWhere,betSelectAndFrom):
    try:
        rows=0
        allrows=[]
        tableData = OrderedDict()
        for cols in allTable[''.join(tableNames)]:
            tableData[cols]= allTable[''.join(tableNames)][cols]
        allcols = tableData.keys()
        while(rows < len(tableData.values()[0])):
            cols = 0
            rowlist = []
            comp1 = False
            comp2 = False
            if afterWhere[1] == ">":
                comp1 = greaterThan(tableData.values()[tableData.keys().index(afterWhere[0])][rows],int(afterWhere[2]))
            elif afterWhere[1] == "<":
                comp1 = lessThan(tableData.values()[tableData.keys().index(afterWhere[0])][rows],int(afterWhere[2]))
            elif afterWhere[1] == "=":
                comp1 = equal(tableData.values()[tableData.keys().index(afterWhere[0])][rows],int(afterWhere[2]))
            elif afterWhere[1] == "@":
                comp1 = lessThanEqual(tableData.values()[tableData.keys().index(afterWhere[0])][rows],int(afterWhere[2]))
            elif afterWhere[1] == "#":
                comp1 = greaterThanEqual(tableData.values()[tableData.keys().index(afterWhere[0])][rows],int(afterWhere[2]))
            elif afterWhere[1] == "$":
                comp1 = notEqual(tableData.values()[tableData.keys().index(afterWhere[0])][rows],int(afterWhere[2]))


            if afterWhere[5] == ">":
                comp2 = greaterThan(tableData.values()[tableData.keys().index(afterWhere[4])][rows],int(afterWhere[6]))
            elif afterWhere[5] == "<":
                comp2 = lessThan(tableData.values()[tableData.keys().index(afterWhere[4])][rows],int(afterWhere[6]))
            elif afterWhere[5] == "=":
                comp2 = equal(tableData.values()[tableData.keys().index(afterWhere[4])][rows],int(afterWhere[6]))
            elif afterWhere[5] == "@":
                comp2 = lessThanEqual(tableData.values()[tableData.keys().index(afterWhere[4])][rows],int(afterWhere[6]))
            elif afterWhere[5] == "#":
                comp2 = greaterThanEqual(tableData.values()[tableData.keys().index(afterWhere[4])][rows],int(afterWhere[6]))
            elif afterWhere[5] == "$":
                comp2 = notEqual(tableData.values()[tableData.keys().index(afterWhere[4])][rows],int(afterWhere[6]))

            if afterWhere[3]=="and":
                if  comp1 and  comp2:
                    while (cols < len(tableData.keys())):
                        rowlist.append(tableData.values()[cols][rows])
                        cols = cols + 1
                    allrows.append(rowlist)
                rows = rows + 1
            elif afterWhere[3]=="or":
                if  comp1 or  comp2:
                    while (cols < len(tableData.keys())):
                        rowlist.append(tableData.values()[cols][rows])
                        cols = cols + 1
                    allrows.append(rowlist)
                rows = rows + 1
        for cols in allcols:
            allcols[allcols.index(cols)] = tableNames[0]+"."+cols
        printResult(allcols,allrows)
    except Exception as e:
        print e
        sys.exit("ERROR CHECK QUERY SYNTAX")


def selectColumnWithOneCondition(tableNames,query,afterWhere,betFromAndWhere,betSelectAndFrom):
    try:
        tableData = OrderedDict()
        for cols in allTable[''.join(tableNames)]:
            tableData[cols]= allTable[''.join(tableNames)][cols]

        tableCols = ''.join(betSelectAndFrom).split(",")

        if "." in betSelectAndFrom:
            for col in tableCols:
                tableCols[tableCols.index(col)]  = col.split(".")[1]

        indexofcols = []

        allrows = []
        allcols = []
        for cols in tableCols:
            allcols.append(cols)
        rows=0
        for col in tableCols:
            indexofcols = allTable[''.join(tableNames)].keys().index(col)
        while(rows < len(tableData.values()[0])):
            cols = 0
            rowlist = []
            comp1 = False

            if afterWhere[1] == "=":
                comp1 = equal(tableData.values()[tableData.keys().index(afterWhere[0])][rows],int(afterWhere[2]))
            elif afterWhere[1] == ">":
                comp1 = greaterThan(tableData.values()[tableData.keys().index(afterWhere[0])][rows],int(afterWhere[2]))
            elif afterWhere[1] == "<":
                comp1 = lessThan(tableData.values()[tableData.keys().index(afterWhere[0])][rows],int(afterWhere[2]))
            elif afterWhere[1] == "@":
                comp1 = lessThanEqual(tableData.values()[tableData.keys().index(afterWhere[0])][rows],int(afterWhere[2]))
            elif afterWhere[1] == "#":
                comp1 = greaterThanEqual(tableData.values()[tableData.keys().index(afterWhere[0])][rows],int(afterWhere[2]))
            elif afterWhere[1] == "$":
                comp1 = notEqual(tableData.values()[tableData.keys().index(afterWhere[0])][rows],int(afterWhere[2]))
            else:
                sys.exit("ERROR: CHECK QUERY SYNTAX")
            if comp1:
                while (cols < len(tableData.keys())):
                    if cols == indexofcols:
                        rowlist.append(tableData.values()[cols][rows])
                    cols = cols + 1
                allrows.append(rowlist)
            rows = rows + 1
        for cols in allcols:
            allcols[allcols.index(cols)] = tableNames[0]+"."+cols
        printResult(allcols,allrows)
    except Exception as e:
        print e
        sys.exit("ERROR: CHECK QUERY SYNTAX")


def selectColumnWithTwoCondition(tableNames,query,afterWhere,betFromAndWhere,betSelectAndFrom):
    try:
        tableData = OrderedDict()
        for cols in allTable[''.join(tableNames)]:
            tableData[cols]= allTable[''.join(tableNames)][cols]
        tableCols = ''.join(betSelectAndFrom).split(",")

        if "." in betSelectAndFrom:
            for col in tableCols:
                tableCols[tableCols.index(col)]  = col.split(".")[1]

        indexofcols = []
        allrows = []
        allcols = []
        for cols in tableCols:
            allcols.append(cols)
        rows=0
        for col in tableCols:
            indexofcols = allTable[''.join(tableNames)].keys().index(col)
        while(rows < len(tableData.values()[0])):
            cols = 0
            rowlist = []

            comp1 = False
            comp2 = False
            if afterWhere[1] == ">":
                comp1 = greaterThan(tableData.values()[tableData.keys().index(afterWhere[0])][rows],int(afterWhere[2]))
            elif afterWhere[1] == "<":
                comp1 = lessThan(tableData.values()[tableData.keys().index(afterWhere[0])][rows],int(afterWhere[2]))
            elif afterWhere[1] == "=":
                comp1 = equal(tableData.values()[tableData.keys().index(afterWhere[0])][rows],int(afterWhere[2]))
            elif afterWhere[1] == "@":
                comp1 = lessThanEqual(tableData.values()[tableData.keys().index(afterWhere[0])][rows],int(afterWhere[2]))
            elif afterWhere[1] == "#":
                comp1 = greaterThanEqual(tableData.values()[tableData.keys().index(afterWhere[0])][rows],int(afterWhere[2]))
            elif afterWhere[1] == "$":
                comp1 = notEqual(tableData.values()[tableData.keys().index(afterWhere[0])][rows],int(afterWhere[2]))


            if afterWhere[5] == ">":
                comp2 = greaterThan(tableData.values()[tableData.keys().index(afterWhere[4])][rows],int(afterWhere[6]))
            elif afterWhere[5] == "<":
                comp2 = lessThan(tableData.values()[tableData.keys().index(afterWhere[4])][rows],int(afterWhere[6]))
            elif afterWhere[5] == "=":
                comp2 = equal(tableData.values()[tableData.keys().index(afterWhere[4])][rows],int(afterWhere[6]))
            elif afterWhere[5] == "@":
                comp2 = lessThanEqual(tableData.values()[tableData.keys().index(afterWhere[4])][rows],int(afterWhere[6]))
            elif afterWhere[5] == "#":
                comp2 = greaterThanEqual(tableData.values()[tableData.keys().index(afterWhere[4])][rows],int(afterWhere[6]))
            elif afterWhere[5] == "$":
                comp2 = notEqual(tableData.values()[tableData.keys().index(afterWhere[4])][rows],int(afterWhere[6]))

            if afterWhere[3]=="and":
                if comp1 and comp2:
                    while (cols < len(tableData.keys())):
                        if cols == indexofcols:
                            rowlist.append(tableData.values()[cols][rows])
                        cols = cols + 1
                    allrows.append(rowlist)
                rows = rows + 1
            elif afterWhere[3]=="or":
                if comp1 or comp2:
                    while (cols < len(tableData.keys())):
                        if cols == indexofcols:
                            rowlist.append(tableData.values()[cols][rows])
                        cols = cols + 1
                    allrows.append(rowlist)
                rows = rows + 1
        for cols in allcols:
            allcols[allcols.index(cols)] = tableNames[0]+"."+cols
        printResult(allcols,allrows)
    except Exception as e:
        print e
        sys.exit("ERROR: CHECK QUERY SYNTAX")



def selectMultiColumnWithOneCondition(tableNames,query,afterWhere,betFromAndWhere,betSelectAndFrom):
    try:
        tableData = OrderedDict()
        for cols in allTable[''.join(tableNames)]:
            tableData[cols]= allTable[''.join(tableNames)][cols]

        tableCols = ''.join(betSelectAndFrom).split(",")

        if "." in betSelectAndFrom:
            for col in tableCols:
                tableCols[tableCols.index(col)]  = col.split(".")[1]

        indexofcols = []
        for cols in tableCols:
            if cols not in allTable[''.join(tableNames)].keys():
                sys.exit("ERROR: COLUMN '"+cols.upper()+"' DOES NOT EXIST IN TABLE")

        rows=0
        allrows = []
        allcols = []
        for col in tableCols:
            indexofcols.append(allTable[''.join(tableNames)].keys().index(col))
            allcols.append(col)

        while(rows < len(tableData.values()[0])):

            cols = 0
            rowlist = []
            comp1 = False

            if afterWhere[1] == "=":
                comp1 = equal(tableData.values()[tableData.keys().index(afterWhere[0])][rows],int(afterWhere[2]))
            elif afterWhere[1] == ">":
                comp1 = greaterThan(tableData.values()[tableData.keys().index(afterWhere[0])][rows],int(afterWhere[2]))
            elif afterWhere[1] == "<":
                comp1 = lessThan(tableData.values()[tableData.keys().index(afterWhere[0])][rows],int(afterWhere[2]))
            elif afterWhere[1] == "@":
                comp1 = lessThanEqual(tableData.values()[tableData.keys().index(afterWhere[0])][rows],int(afterWhere[2]))
            elif afterWhere[1] == "#":
                comp1 = greaterThanEqual(tableData.values()[tableData.keys().index(afterWhere[0])][rows],int(afterWhere[2]))
            elif afterWhere[1] == "$":
                comp1 = notEqual(tableData.values()[tableData.keys().index(afterWhere[0])][rows],int(afterWhere[2]))
            else:
                sys.exit("ERROR: CHECK QUERY SYNTAX")
            if comp1:
                while (cols < len(indexofcols)):
                    rowlist.append(tableData.values()[indexofcols[cols]][rows])
                    cols = cols + 1
                allrows.append(rowlist)
            rows = rows + 1
        for cols in allcols:
            allcols[allcols.index(cols)] = tableNames[0]+"."+cols
        printResult(allcols,allrows)
    except Exception as e:
        print e
        sys.exit("ERROR: CHECK QUERY SYNTAX")



def selectMultiColumnWithTwoCondition(tableNames,query,afterWhere,betFromAndWhere,betSelectAndFrom):
    try:
        tableData = OrderedDict()
        for cols in allTable[''.join(tableNames)]:
            tableData[cols]= allTable[''.join(tableNames)][cols]
        tableCols = ''.join(betSelectAndFrom).split(",")

        if "." in betSelectAndFrom:
            for col in tableCols:
                tableCols[tableCols.index(col)]  = col.split(".")[1]

        rows=0
        indexofcols = []
        for cols in tableCols:
            if cols not in allTable[''.join(tableNames)].keys():
                sys.exit("ERROR: COLUMN '"+cols.upper()+"' DOES NOT EXIST IN TABLE")
        allrows = []
        allcols = []
        for col in tableCols:
            indexofcols.append(allTable[''.join(tableNames)].keys().index(col))
            allcols.append(col)
        while(rows < len(tableData.values()[0])):
            cols = 0
            rowlist = []
            comp1 = False
            comp2 = False
            if afterWhere[1] == ">":
                comp1 = greaterThan(tableData.values()[tableData.keys().index(afterWhere[0])][rows],int(afterWhere[2]))
            elif afterWhere[1] == "<":
                comp1 = lessThan(tableData.values()[tableData.keys().index(afterWhere[0])][rows],int(afterWhere[2]))
            elif afterWhere[1] == "=":
                comp1 = equal(tableData.values()[tableData.keys().index(afterWhere[0])][rows],int(afterWhere[2]))
            elif afterWhere[1] == "@":
                comp1 = lessThanEqual(tableData.values()[tableData.keys().index(afterWhere[0])][rows],int(afterWhere[2]))
            elif afterWhere[1] == "#":
                comp1 = greaterThanEqual(tableData.values()[tableData.keys().index(afterWhere[0])][rows],int(afterWhere[2]))
            elif afterWhere[1] == "$":
                comp1 = notEqual(tableData.values()[tableData.keys().index(afterWhere[0])][rows],int(afterWhere[2]))


            if afterWhere[5] == ">":
                comp2 = greaterThan(tableData.values()[tableData.keys().index(afterWhere[4])][rows],int(afterWhere[6]))
            elif afterWhere[5] == "<":
                comp2 = lessThan(tableData.values()[tableData.keys().index(afterWhere[4])][rows],int(afterWhere[6]))
            elif afterWhere[5] == "=":
                comp2 = equal(tableData.values()[tableData.keys().index(afterWhere[4])][rows],int(afterWhere[6]))
            elif afterWhere[5] == "@":
                comp2 = lessThanEqual(tableData.values()[tableData.keys().index(afterWhere[4])][rows],int(afterWhere[6]))
            elif afterWhere[5] == "#":
                comp2 = greaterThanEqual(tableData.values()[tableData.keys().index(afterWhere[4])][rows],int(afterWhere[6]))
            elif afterWhere[5] == "$":
                comp2 = notEqual(tableData.values()[tableData.keys().index(afterWhere[4])][rows],int(afterWhere[6]))
            if afterWhere[3]=="and":
                if  comp1 and  comp2:
                    while (cols < len(indexofcols)):
                        rowlist.append(tableData.values()[indexofcols[cols]][rows])
                        cols = cols + 1
                    allrows.append(rowlist)
                rows = rows + 1
            elif afterWhere[3]=="or":
                if  comp1 or  comp2:
                    while (cols < len(indexofcols)):
                        rowlist.append(tableData.values()[indexofcols[cols]][rows])
                        cols = cols + 1
                    allrows.append(rowlist)
                rows = rows + 1
            else:
                sys.exit("ERROR: CHECK QUERY SYNTAX")
        for cols in allcols:
            allcols[allcols.index(cols)] = tableNames[0]+"."+cols
        printResult(allcols,allrows)
    except Exception as e:
        print e
        sys.exit("ERROR: CHECK QUERY SYNTAX")



def selectMultiWithDotAndOneCondition(tableNames,query,afterWhere,betFromAndWhere,betSelectAndFrom):
    try:
        condition = afterWhere[3]
        tnames = [afterWhere[0],afterWhere[4]]
        for t in tnames:
            if t not in tableNames:
                sys.exit("ERROR: "+t+" NOT IN "+ tableNames[0])

        if "*" not in betSelectAndFrom:
            tableCols = ''.join(betSelectAndFrom).split(",")
            for c in tableCols:
                if c not in allTable[tableNames[0]].keys():
                    sys.exit("COLUMN "+c+" NOT PRESENT IN TABLE")
        else:
            tableCols = allTable[tableNames[0]].keys()

        # cols = [afterWhere[2],afterWhere[6]]
        tableData = OrderedDict()

        for c in allTable[''.join(tableNames)]:
            tableData[c]= allTable[''.join(tableNames)][c]
        # tableCols = ''.join(betSelectAndFrom).split(",")

        # print tableCols

        indexofcols = []

        rows=0
        allrows = []
        allcols = []

        for col in tableCols:
            indexofcols.append(allTable[''.join(tableNames)].keys().index(col))
            allcols.append(col)

        while(rows < len(tableData.values()[0])):

            cols = 0
            rowlist = []
            comp1 = False

            if condition == "=":
                comp1 = equal(tableData.values()[tableData.keys().index(afterWhere[2])][rows],tableData.values()[tableData.keys().index(afterWhere[6])][rows])
            elif condition == ">":
                comp1 = greaterThan(tableData.values()[tableData.keys().index(afterWhere[2])][rows],tableData.values()[tableData.keys().index(afterWhere[6])][rows])
            elif condition == "<":
                comp1 = lessThan(tableData.values()[tableData.keys().index(afterWhere[2])][rows],tableData.values()[tableData.keys().index(afterWhere[6])][rows])
            elif condition == "@":
                comp1 = lessThanEqual(tableData.values()[tableData.keys().index(afterWhere[2])][rows],tableData.values()[tableData.keys().index(afterWhere[6])][rows])
            elif condition == "#":
                comp1 = greaterThanEqual(tableData.values()[tableData.keys().index(afterWhere[2])][rows],tableData.values()[tableData.keys().index(afterWhere[6])][rows])
            elif condition == "$":
                comp1 = notEqual(tableData.values()[tableData.keys().index(afterWhere[2])][rows],tableData.values()[tableData.keys().index(afterWhere[6])][rows])
            else:
                sys.exit("ERROR: CHECK QUERY SYNTAX")
            if comp1:
                while (cols < len(indexofcols)):
                    rowlist.append(tableData.values()[indexofcols[cols]][rows])
                    cols = cols + 1
                allrows.append(rowlist)
            rows = rows + 1
        for cols in allcols:
            allcols[allcols.index(cols)] = tableNames[0]+"."+cols
        printResult(allcols,allrows)
    except Exception as e:
        print e
        sys,exit("ERROR: PLEASE CHECK QUERY SYNTAX")

        
def selectMultiWithDotAndTwoCondition(tableNames,query,afterWhere,betFromAndWhere,betSelectAndFrom):
    try:
        # print "Entered"
        condition1 = afterWhere[3]
        condition2 = afterWhere[11]
        tnames = [afterWhere[0],afterWhere[4],afterWhere[8],afterWhere[12]]
        for t in tnames:
            if t not in tableNames:
                sys.exit("ERROR: "+t+" NOT IN "+ tableNames[0])

        if "*" not in betSelectAndFrom:
            tableCols = ''.join(betSelectAndFrom).split(",")
            for c in tableCols:
                if c not in allTable[tableNames[0]].keys():
                    sys.exit("COLUMN "+c+" NOT PRESENT IN TABLE")
        else:
            tableCols = allTable[tableNames[0]].keys()


        # cols = [afterWhere[2],afterWhere[6]]
        tableData = OrderedDict()

        for c in allTable[''.join(tableNames)]:
            tableData[c]= allTable[''.join(tableNames)][c]
        # tableCols = ''.join(betSelectAndFrom).split(",")

        # print tableCols

        indexofcols = []

        rows=0
        allrows = []
        allcols = []

        for col in tableCols:
            indexofcols.append(allTable[''.join(tableNames)].keys().index(col))
            allcols.append(col)

        while(rows < len(tableData.values()[0])):
            cols = 0
            rowlist = []
            comp1 = False
            comp2 = False
            if condition1 == "=":
                comp1 = equal(tableData.values()[tableData.keys().index(afterWhere[2])][rows],tableData.values()[tableData.keys().index(afterWhere[6])][rows])
            elif condition1 == ">":
                comp1 = greaterThan(tableData.values()[tableData.keys().index(afterWhere[2])][rows],tableData.values()[tableData.keys().index(afterWhere[6])][rows])
            elif condition1 == "<":
                comp1 = lessThan(tableData.values()[tableData.keys().index(afterWhere[2])][rows],tableData.values()[tableData.keys().index(afterWhere[6])][rows])
            elif condition1 == "@":
                comp1 = lessThanEqual(tableData.values()[tableData.keys().index(afterWhere[2])][rows],tableData.values()[tableData.keys().index(afterWhere[6])][rows])
            elif condition1 == "#":
                comp1 = greaterThanEqual(tableData.values()[tableData.keys().index(afterWhere[2])][rows],tableData.values()[tableData.keys().index(afterWhere[6])][rows])
            elif condition1 == "$":
                comp1 = notEqual(tableData.values()[tableData.keys().index(afterWhere[2])][rows],tableData.values()[tableData.keys().index(afterWhere[6])][rows])
            else:
                sys.exit("ERROR: CHECK QUERY SYNTAX")


            if condition2 == "=":
                comp2 = equal(tableData.values()[tableData.keys().index(afterWhere[10])][rows],tableData.values()[tableData.keys().index(afterWhere[14])][rows])
            elif condition2 == ">":
                comp2 = greaterThan(tableData.values()[tableData.keys().index(afterWhere[10])][rows],tableData.values()[tableData.keys().index(afterWhere[14])][rows])
            elif condition2 == "<":
                comp2 = lessThan(tableData.values()[tableData.keys().index(afterWhere[10])][rows],tableData.values()[tableData.keys().index(afterWhere[14])][rows])
            elif condition2 == "@":
                comp2 = lessThanEqual(tableData.values()[tableData.keys().index(afterWhere[10])][rows],tableData.values()[tableData.keys().index(afterWhere[14])][rows])
            elif condition2 == "#":
                comp2 = greaterThanEqual(tableData.values()[tableData.keys().index(afterWhere[10])][rows],tableData.values()[tableData.keys().index(afterWhere[14])][rows])
            elif condition2 == "$":
                comp2 = notEqual(tableData.values()[tableData.keys().index(afterWhere[10])][rows],tableData.values()[tableData.keys().index(afterWhere[14])][rows])
            else:
                sys.exit("ERROR: CHECK QUERY SYNTAX")

            # print "H"
            if afterWhere[7]=="and":
                if  comp1 and  comp2:
                    while (cols < len(indexofcols)):
                        rowlist.append(tableData.values()[indexofcols[cols]][rows])
                        cols = cols + 1
                    allrows.append(rowlist)
                rows = rows + 1
            elif afterWhere[7]=="or":
                if  comp1 or  comp2:
                    while (cols < len(indexofcols)):
                        rowlist.append(tableData.values()[indexofcols[cols]][rows])
                        cols = cols + 1
                    allrows.append(rowlist)
                rows = rows + 1
            else:
                sys.exit("ERROR: CHECK QUERY SYNTAX")
        for cols in allcols:
            allcols[allcols.index(cols)] = tableNames[0]+"."+cols
        printResult(allcols,allrows)
    except Exception as e:
        print e
        sys.exit("PLEASE CHECK QUERY SYNTAX")

def whereWithOneTable(tableNames,query,afterWhere,betFromAndWhere,betSelectAndFrom):
    try:
        # print len(afterWhere)
        # print betSelectAndFrom
        tableData = OrderedDict()
        for cols in allTable[''.join(tableNames)]:
            tableData[cols]= allTable[''.join(tableNames)][cols]
            tableCols = ''.join(betSelectAndFrom).split(",")
        if len(tableCols) == 1 and "." not in afterWhere:
            colSelect = ''.join(tableCols)
            if "*" == colSelect:
                if len(afterWhere) == 3:
                    selectAllWithOneCondition(tableNames,query,afterWhere,betFromAndWhere,betSelectAndFrom)
                elif len(afterWhere) == 7:
                    selectAllWithTwoCondition(tableNames,query,afterWhere,betFromAndWhere,betSelectAndFrom)
                else:
                    sys.exit("ERROR: SYNTAX ERROR")
            elif query[1] in allTable[''.join(tableNames)].keys() :
                if len(afterWhere) == 3:
                    selectColumnWithOneCondition(tableNames,query,afterWhere,betFromAndWhere,betSelectAndFrom)
                elif len(afterWhere) == 7:
                    selectColumnWithTwoCondition(tableNames,query,afterWhere,betFromAndWhere,betSelectAndFrom)
                else:
                    sys.exit("ERROR: CHECK QUERY SYNTAX")
            elif "." in betSelectAndFrom :
                if len(afterWhere) == 3:
                    selectColumnWithOneCondition(tableNames,query,afterWhere,betFromAndWhere,betSelectAndFrom)
                elif len(afterWhere) == 7:
                    selectColumnWithTwoCondition(tableNames,query,afterWhere,betFromAndWhere,betSelectAndFrom)
                else:
                    sys.exit("ERROR: CHECK QUERY SYNTAX")
            else:
                sys.exit("ERROR: COLUMN DOES NOT EXIST IN TABLE")
        else:
            if len(afterWhere) == 3 and "." not in afterWhere:
                selectMultiColumnWithOneCondition(tableNames,query,afterWhere,betFromAndWhere,betSelectAndFrom)
            elif len(afterWhere) == 7 and "." not in afterWhere:
                selectMultiColumnWithTwoCondition(tableNames,query,afterWhere,betFromAndWhere,betSelectAndFrom)
            elif len(afterWhere) == 7 and "." in afterWhere:
                selectMultiWithDotAndOneCondition(tableNames,query,afterWhere,betFromAndWhere,betSelectAndFrom)
            elif len(afterWhere) == 15 and "." in afterWhere:
                # print "going"
                selectMultiWithDotAndTwoCondition(tableNames,query,afterWhere,betFromAndWhere,betSelectAndFrom)
            else:
                sys.exit("ERROR CHECK QUERY SYNTAX")
    except Exception as e:
        print e
        sys.exit("ERROR: CHECK QUERY SYNTAX")
