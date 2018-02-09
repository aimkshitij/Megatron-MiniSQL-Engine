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





def selectAllQuery(query):
    try:
        if len(list(sys.argv[1].split())) == 4 and "," not in query[3]:
            tableName = tableNameFind()
            rows=0
            allrows=[]
            allcols=allTable[tableName].keys()
            while(rows < len(allTable[tableName].values()[0])):
                cols = 0
                rowlist = []
                while (cols < len(allTable[tableName].keys())):
                    rowlist.append(allTable[tableName].values()[cols][rows])
                    cols = cols + 1
                rows = rows + 1
                allrows.append(rowlist)
            for cols in allcols:
                allcols[allcols.index(cols)] = tableName+"."+cols
            printResult(allcols,allrows)
        elif query[2] == "from" :
            try:
                tableNames = query[3:]
                tableNames = ''.join(tableNames)
                tableNames = tableNames.rstrip(";")
                tableNames = tableNames.split(",")

                newTable = cartesianProduct(tableNames)
                table1Keys = allTable[tableNames[0]].keys()
                for keys in table1Keys:
                    table1Keys[table1Keys.index(keys)] = tableNames[0]+"."+keys
                table2Keys = allTable[tableNames[1]].keys()
                for keys in table2Keys:
                    table2Keys[table2Keys.index(keys)] = tableNames[1]+"."+keys
                allcols = table1Keys + table2Keys
                printResult(allcols,newTable)
            except:
                sys.exit("ERROR: CHECK SELECT ALL QUERY SYNTAX!!")
        else:
            sys.exit("ERROR: CHECK SELECT ALL QUERY SYNTAX!!")

    except Exception as e:
        print e
        sys.exit("ERROR: OCCURED IN PROCESSING SELECT ALL QUERY")
