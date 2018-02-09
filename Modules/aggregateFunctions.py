import sys
from databasefile import *
from cartesianProduct import *
from printResult import *




def tableNameFind():
    try:
        tableName =  list(sys.argv[1].split())[-1].split(';')[0].lower()
        dataTables = allTable.keys()
        for data in dataTables:
            data.lower()
        if tableName in dataTables:
            return tableName
        else:
            sys.exit("ERROR: TABLE '"+ list(sys.argv[1].split())[3].split(';')[0]+"' NOT EXIST IN DATABASE!!")
    except Exception as e:
        print e;
        sys.exit("ERROR OCCURED IN FINDING TABLE NAME")





def multiTableAggregateFunc(tableNames,betSelectAndFrom):
    try:
        for t in tableNames:
            if t not in allTable.keys():
                sys.exit("ERROR: TABLE "+t+" DOES NOT EXIST IN DATABASE")
        allrows=cartesianProduct(tableNames)
        # print betSelectAndFrom
        if len(betSelectAndFrom)!=1 or len(tableNames) > 2:
            sys.exit("CHECK SYNTAX OR SUCH KIND OF QUERY NOT SUPPORTED")
        if "." in betSelectAndFrom[0]:
            col = betSelectAndFrom[0].split(".")[1].split(")")[0]
            aggTName  = betSelectAndFrom[0].split("(")[1].split(".")[0]
            if aggTName not in tableNames:
                sys.exit("ERROR: UNKNOWN COLUMN "+ ''.join(betSelectAndFrom))
        else:
            col = betSelectAndFrom[0].split("(")[1].split(")")[0]

        allKeys = allTable[tableNames[0]].keys() + allTable[tableNames[1]].keys()
        # print allKeys
        if col not in allKeys:
            sys.exit("ERROR: COLUMN "+col+" DOES NOT EXIST IN ANY TABLE")



        indexOfCol = ''

        if col in allTable[tableNames[0]].keys() and col in allTable[tableNames[1]].keys():
            if aggTName == tableNames[0]:
                indexOfCol = allKeys.index(col)
            else:
                indexOfCol = allKeys.index(col) + len(allTable[tableNames[0]].keys())
        else:
            indexOfCol = allKeys.index(col)
        AggAllCol = []
        for row in allrows:
            AggAllCol.append(row[indexOfCol])

        aFunc = betSelectAndFrom[0].split("(")[0]

        colTable = ''
        for t in tableNames:
            if col in allTable[t].keys():
                colTable = t
        if "." not in betSelectAndFrom[0]:
            resultCol = aFunc+"("+colTable+"."+col+")"
        else:
            resultCol = ''.join(betSelectAndFrom)
        if aFunc == "sum":
            printResult([resultCol],[sum(AggAllCol)])
        elif aFunc == "max":
            printResult([resultCol],[max(AggAllCol)])
        elif aFunc == "min":
            printResult([resultCol],[min(AggAllCol)])
        elif aFunc == "count":
            printResult([resultCol],[len(AggAllCol)])
        elif aFunc == "avg":
            printResult([resultCol],[float(sum(AggAllCol))/len(AggAllCol)])
        else:
            sys.exit("ERROR: CHECK QUERY SYNTAX")
    except Exception as e:
        print e
        sys.exit("ERROR: CHECK AGGREGATE FUNCTION QUERY SYNTAX")


def aggeregateParsing():

    #print "Aggregate Function Found in Query"
    try:
        query = sys.argv[1]
        query = query.split()
        for word in query:
            query[query.index(word)] = word.lower()



        fromIndex =  query.index("from")
        betSelectAndFrom = query[ 1 :fromIndex ]
        betSelectAndFrom = ''.join(betSelectAndFrom).split(",")
        afterFrom = query[fromIndex+1:]
        tableNames =  ''.join(afterFrom).split(",")
        # print tableNames
        for tName in tableNames:
            if len(tableNames) != 1:
                multiTableAggregateFunc(tableNames,betSelectAndFrom)
                sys.exit()
            if tName not in allTable.keys() :
                sys.exit("ERROR: TABLE '" + tName+"' DOES NOT EXIT IN DATABASE")

        if "(" not in list(sys.argv[1].split())[1]:
            sys.exit("ERROR: CHECK AGGREGATE FUNCTION QUERY SYNTAX!!")
        if ")" not in list(sys.argv[1].split())[1]:
            sys.exit("ERROR: CHECK AGGREGATE FUNCTION QUERY SYNTAX!!")
        aggFunc = list(sys.argv[1].split())[1].split('(')[0]
        aggFuncCol = list(sys.argv[1].split())[1].split('(')[1].split(')')[0].lower()

        if len(tableNames) == 1 and len(betSelectAndFrom)==1:
            # print betSelectAndFrom
            # print len(tableNames)
            tableName = tableNameFind()
            TableCols = allTable[tableName].keys()
            for data in TableCols:
                data.lower()
            if "." in aggFuncCol:
                if tableNames[0] == aggFuncCol.split(".")[0]:
                    aggFuncCol = aggFuncCol.split(".")[1]

            if aggFuncCol in TableCols:
                col = aggFunc+"("+tableName+"."+aggFuncCol+")"
                if aggFunc.lower() == "sum":
                    printResult([col],[sum(allTable[tableName][aggFuncCol])])
                elif aggFunc.lower() == "max":
                    printResult([col],[max(allTable[tableName][aggFuncCol])])
                elif aggFunc.lower() == "min":
                    printResult([col],[min(allTable[tableName][aggFuncCol])])
                elif aggFunc.lower() == "avg":
                    printResult([col],[format(float(sum(allTable[tableName][aggFuncCol]))/len(allTable[tableName][aggFuncCol]),'.2f')])
                elif aggFunc.lower() == "count":
                    printResult([col],[len(allTable[tableName][aggFuncCol])])

            else:
                sys.exit("ERROR: UNKNOWN COLUMN '"+list(sys.argv[1].split())[1].split('(')[1].split(')')[0] +"' IN FIELD LIST OF '"+ list(sys.argv[1].split())[3].split(';')[0]+"'")



        elif len(betSelectAndFrom)==1:
            tableCols = []
            columnsIndex = 0
            for tName in tableNames:
                for data in allTable[tName].keys():
                    tableCols.append(data)
            if "." in aggFuncCol:
                aggTableN = aggFuncCol.split(".")[0]
                aggTableC = aggFuncCol.split(".")[1]

                if aggFuncCol.split(".")[0] in tableNames:
                    aggFuncCol = aggFuncCol.split(".")[1]
                else:
                    sys.exit("ERROR: UNKNOWN COLUMN '"+list(sys.argv[1].split())[1].split('(')[1].split(')')[0] +"' IN FIELD LIST")
                if aggFuncCol not in allTable[aggTableN].keys():
                    sys.exit("ERROR: '"+ aggFuncCol+"' DOES NOT EXIST IN '"+aggTableN+"'")

                if tableNames.index(aggTableN) == 1:
                    columnsIndex = allTable[aggTableN].keys().index(aggTableC) + len(allTable[tableNames[0]].keys())
                else:
                    columnsIndex = allTable[aggTableN].keys().index(aggTableC)
            else:
                tcol = []
                for tName in tableNames:
                    for cols in  allTable[tName].keys():
                        tcol.append(cols)
                if tcol.count(aggFuncCol)!=1:
                    sys.exit("ERROR: AMBIGIOUS COLUMN IN LIST FIELD")
                columnsIndex = allTable[tableNames[0]].keys().index(aggFuncCol)
            tableData = cartesianProduct(tableNames)
            aggColRows = []
            for rows in tableData:
                aggColRows.append(rows[columnsIndex])

            if aggFunc == "max":
                printResult([sys.argv[1].split()[1]],[max(aggColRows)])
            elif aggFunc == "min":
                printResult([sys.argv[1].split()[1]],[min(aggColRows)])
            elif aggFunc == "sum":
                printResult([sys.argv[1].split()[1]],[sum(aggColRows)])
            elif aggFunc == "avg":
                printResult([sys.argv[1].split()[1]],[format(float(sum(aggColRows))/len(aggColRows),'.2f')])
            elif aggFunc == "count":
                printResult([sys.argv[1].split()[1]],[len(aggColRows)])
        elif len(betSelectAndFrom)!=1:
            agFunc = []
            for func in betSelectAndFrom:
                agFunc.append(func.split("(")[0])
            # print agFunc
            agCol = []
            tableName = tableNames[0]
            for func in betSelectAndFrom:
                agCol.append(func.split("(")[1].split(")")[0])
            for c in agCol:
                if c not in allTable[tableName].keys():
                    sys.exit("COLUMN "+c+" DOES NOT EXIST IN "+tableName)
            # print agCol
            # print tableName
            funcs = []
            funcResults = []
            totalFunc = len(agCol)
            for i in range(totalFunc):
                if agFunc[i]=="max":
                    col = agFunc[i]+"("+tableName+"."+agCol[i]+")"
                    funcs.append(col)
                    funcResults.append(max(allTable[tableName][agCol[i]]))
                if agFunc[i]=="min":
                    col = agFunc[i]+"("+tableName+"."+agCol[i]+")"
                    funcs.append(col)
                    funcResults.append(min(allTable[tableName][agCol[i]]))
                if agFunc[i]=="sum":
                    col = agFunc[i]+"("+tableName+"."+agCol[i]+")"
                    funcs.append(col)
                    funcResults.append(sum(allTable[tableName][agCol[i]]))
                if agFunc[i]=="count":
                    col = agFunc[i]+"("+tableName+"."+agCol[i]+")"
                    funcs.append(col)
                    funcResults.append(len(allTable[tableName][agCol[i]]))
                if agFunc[i]=="avg":
                    col = agFunc[i]+"("+tableName+"."+agCol[i]+")"
                    funcs.append(col)
                    funcResults.append(float(format(float(sum(allTable[tableName][agCol[i]]))/len(allTable[tableName][agCol[i]]),'.2f')))

            print ','.join(funcs)
            print ','.join(str(x) for x in funcResults)
            # print funcResults
            # print ','.join(funcResults)
            # printResult(funcs,funcResults)

        else:
            sys.exit("ERROR: CHECK QUERY SYNTAX")
    except Exception as e:
        print e
        sys.exit("ERROR: CHECK AGGREGATE FUNCTION QUERY SYNTAX!!")
