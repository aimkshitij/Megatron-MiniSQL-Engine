#from __future__ import print_function
import sys
import csv
sys.path.append('Modules')
# sys.path.append('Modules/prettytable-0.7.2')

from databasefile import *
from aggregateFunctions import *
from cartesianProduct import *
from selectAllQuery import *
from distinctProcessing import *
from selectColumnProcessing import *
from whereWithOneTable import *
from whereWithTwoTable import *

from collections import OrderedDict
from prettytable import PrettyTable
import re
import timeit
import copy





#CHECK WWHETHER TABLE NAME EXIST IN DATABASE OF NOT AND RETURN TABLE NAME IF TABL EXIST
def tableNameFind():
    tableName =  list(sys.argv[1].split())[-1].split(';')[0].lower()
    dataTables = allTable.keys()
    for data in dataTables:
        data.lower()
    if tableName in dataTables:
        return tableName
    else:
        sys.exit("ERROR: TABLE '"+ list(sys.argv[1].split())[3].split(';')[0]+"' NOT EXIST IN DATABASE!!")


def processWhereQuery():
    query = sys.argv[1]

    if "<=" in query:
        query = query.replace("<="," @ ")
    if ">=" in query:
        query = query.replace(">="," # ")
    if "!=" in query:
        query = query.replace("!="," $ ")
    if "<" in query:
        query = query.replace("<"," < ")
    if "." in query:
        query = query.replace("."," . ")
    if "=" in query:
        query = query.replace("="," = ")
    if "," in query:
        query = query.replace(","," , ")
    if ">" in query:
        query = query.replace(">"," > ")

    query = query.split()
    for word in query:
        query[query.index(word)] = word.lower()
    fromIndex =  query.index("from")
    betSelectAndFrom = query[ 1 :fromIndex ]
    whereIndex = query.index("where")
    betFromAndWhere = query[fromIndex+1:whereIndex]
    afterWhere = query[whereIndex+1:]

    tableNames =  ''.join(betFromAndWhere).split(",")
    for tName in tableNames:
        if tName not in allTable.keys():
            sys.exit("ERROR: table '" + tName+"' DOES NOT EXIT IN DATABASE")

    if len(tableNames) == 1:
        whereWithOneTable(tableNames,query,afterWhere,betFromAndWhere,betSelectAndFrom)
    else:
        whereWithTwoTable(tableNames,query,afterWhere,betFromAndWhere,betSelectAndFrom)

def parseQuery():
    query = sys.argv[1].split()
    for word in query:
        query[query.index(word)] = word.lower()

    if query[0].lower() != "select":
        sys.exit("ERROR: SELECT STATEMENT NOT FOUND!!")

    if "from" not in query:
        sys.exit("ERROR: FROM STATEMENT NOT FOUND IN QUERY!!")

    aggregate = ['sum','max','min','avg','count']
    for aggr in aggregate:
        if aggr in query[1].lower():
            aggeregateParsing()
            return

    if "where" in query:
        processWhereQuery()
        sys.exit()
    elif query[1].lower() == '*':
        selectAllQuery(query)

    elif "distinct" in query[1].lower():
        distinctProcessing(query)

    elif "where" not in sys.argv[1]:
        selectColumnProcessing(query)
    else:
        sys.exit("ERROR: PLEASE CHECK QUERY SYNTAX")

def main():
    parseQuery()


if __name__ == "__main__":
    try:
        if len(sys.argv) == 1:
            sys.exit("ERROR: SQL COMMAND NOT FOUND!!")
        elif len(sys.argv) > 2:
            sys.exit("ERROR: ENTER VALID NO OF ARGUMENTS")
        createTables()
        main()
    except Exception as e:
        print e
        sys.exit("ERROR: PLEASE CHECK QUERY SYNTAX")
