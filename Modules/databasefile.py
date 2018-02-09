import sys
import csv
import os
import shlex
from collections import OrderedDict


tableMetaData = OrderedDict()
allTable = OrderedDict()
####################################################################################
# To store Data from metadata.txt
def storeTableMeta():
    metafile = open("metadata.txt")
    metafiledata = metafile.readlines()
    flagTName = False
    flagTcolName = False
    for line in metafiledata:
        if line.strip() == "<begin_table>":
            flagTName = True
            continue
        if flagTName:
            tempTableName = line.strip()
            tableMetaData[line.strip()]=[]
            flagTName = False
            flagTcolName = True
            continue
        if line.strip() == "<end_table>":
            flagTcolName = False
        if flagTcolName:
            tableMetaData[tempTableName].append(line.strip().lower())
####################################################################################


####################################################################################
# To store table data in dictonary of tables
def storeTableData():
    for tname in tableMetaData:
        allTable[tname]=OrderedDict()
        for colName in tableMetaData[tname]:
            allTable[tname][colName]=[]


        csvName = tname + ".csv"
        if (os.path.isfile(csvName)):
            with open(csvName, 'rb') as csvfile:
                csvData = csv.reader(csvfile)
                for row in csvData:
                    temp1=0
                    for col in row:
                        temp=0
                        for colName in tableMetaData[tname]:
                            if temp1==temp:
                                if "\"" in col or "\'" in col:
                                    col = ''.join(shlex.split(col))
                                allTable[tname][colName].append(int(col))
                            temp = temp + 1
                        temp1 = temp1 + 1
        else :
            sys.exit("ERROR: Table File Named '" + csvName + "' NOT FOUND!!")
####################################################################################


####################################################################################
#Creating Dictionary of all tables with their data
def createTables():
    try:
        storeTableMeta()
        #tableMetaData = sorted(tableMetaData.iterkeys())
        storeTableData()
    except Exception as e:
        print e
        sys.exit("ERROR: DATABASE CREATION ERROR")
####################################################################################
