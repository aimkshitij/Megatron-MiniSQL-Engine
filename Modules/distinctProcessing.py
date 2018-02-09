import sys
from databasefile import *
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





def distinctProcessing(query):
    try:
        queryitems = []

        distinctCount = 0
        for value in query:
            if "distinct" in value:
                distinctCount = distinctCount + 1;
        if distinctCount > 1:
             sys.exit("ERROR: UNEXPECTED NUMBER OF DISTINCT IN QUERY!!")

        if "(" in query[1] and ")" in query[1]:
            colName = list(sys.argv[1].split())[1].split('(')[1].split(')')[0].lower()
            if len(list(sys.argv[1].split())) != 4:
                sys.exit("ERROR: CHECK DISTINCT QUERY SYNTAX!!")
            tableName = tableNameFind()
            TableCols = allTable[tableName].keys()
            for data in TableCols:
                data.lower()
            # print colName
            if "," in colName:
                sys.exit("ERROR: CHECK DISTINCT QUERY SYNTAX!!")
                # uncomment below code for distinct(c1,c1,..cn) kind of query
                # colName = colName.split(",")
                # for col in colName:
                #     if col not in TableCols:
                #         sys.exit("ERROR: COLUMN '"+col +"' DOES NOT EXIST IN '"+ list(sys.argv[1].split())[3].split(';')[0]+"'")
                # rows = 0
                # indexofcols = []
                # allrows = []
                # for col in colName:
                #     indexofcols.append(allTable[tableName].keys().index(col))
                # while(rows < len(allTable[tableName].values()[0])):
                #     cols = 0
                #     distinctRows = []
                #     while (cols < len(colName)):
                #         distinctRows.append(allTable[tableName].values()[indexofcols[cols]][rows])
                #         cols = cols + 1
                #     rows = rows + 1
                #     if distinctRows not in allrows:
                #         allrows.append(distinctRows)
                # printResult(list(sys.argv[1].split())[1].split('(')[1].split(')')[0].split(","),allrows)


            else:
                if colName in TableCols:
                    distinctRows = []
                    column = tableName+"."+colName
                    for col in allTable[tableName][colName]:
                        if [col] not in distinctRows:
                            distinctRows.append([col])
                    printResult([column],distinctRows)
                elif colName =="*":
                    rows = 0
                    indexofcols = []
                    allrows = []
                    columns = allTable[tableName].keys()
                    for col in columns:
                        indexofcols.append(allTable[tableName].keys().index(col))
                    while(rows < len(allTable[tableName].values()[0])):
                        cols = 0
                        distinctRows = []
                        while (cols < len(columns)):
                            distinctRows.append(allTable[tableName].values()[indexofcols[cols]][rows])
                            cols = cols + 1
                        rows = rows + 1
                        if distinctRows not in allrows:
                            allrows.append(distinctRows)
                    for cols in columns:
                        columns[columns.index(cols)] = tableName+"."+cols
                    printResult(columns,allrows)
                else:
                    sys.exit("ERROR: COLUMN '"+list(sys.argv[1].split())[1].split('(')[1].split(')')[0] +"' DOES NOT EXIST IN '"+ list(sys.argv[1].split())[3].split(';')[0]+"'")

        elif "(" in query[1]:
            sys.exit("ERROR: CHECK DISTINCT QUERY SYNTAX!!")
        elif ")" in query[1]:
            sys.exit("ERROR: CHECK DISTINCT QUERY SYNTAX!!")

        if len(query) > 4 and "(" not in query[1] and ")" not in query[1]:
            cols = []
            cols = query[2:-2]
            if "*" not in cols:
                while "," in cols:
                    cols.remove(',')
                columns = []
                for val in cols:
                    if "," in val:
                        loc = cols.index(val)
                        temp = val.split(",")
                        for item in temp:
                            columns.append(item.strip(","))
                        continue
                    columns.append(val.strip(","))
                while '' in columns:
                    columns.remove('')


                tableName = tableNameFind()
                TableCols = allTable[tableName].keys()
                columns = map(str.lower,columns)

                for col in columns:
                    if col.lower() not in TableCols:
                        sys.exit("ERROR: COLUMN '"+col +"' DOES NOT EXIST IN '"+ tableName+"'")


            elif "*" in cols:
                tableName = tableNameFind()
                columns = allTable[tableName].keys()
            rows = 0
            indexofcols = []
            allrows = []

            for col in columns:
                indexofcols.append(allTable[tableName].keys().index(col))
            while(rows < len(allTable[tableName].values()[0])):
                cols = 0
                distinctRows = []
                while (cols < len(columns)):
                    distinctRows.append(allTable[tableName].values()[indexofcols[cols]][rows])
                    cols = cols + 1
                rows = rows + 1
                if distinctRows not in allrows:
                    allrows.append(distinctRows)
            for cols in columns:
                columns[columns.index(cols)] = tableName+"."+cols
            printResult(columns,allrows)

    except Exception as e:
        print e# -*- coding: utf-8 -*-
        sys.exit("ERROR: OCCURED IN DISTINCT PARSING PLEASE CHECK SYNTAX MANUALLY")
