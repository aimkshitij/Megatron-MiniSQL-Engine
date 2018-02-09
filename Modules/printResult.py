import sys
from databasefile import *
from prettytable import PrettyTable
import timeit


start = timeit.timeit()

# def printResult(col,row):
#     try:
#         length = str(len(row))
#         if len(col)==1:
#             c= ",".join(map(str, col))
#             print c
#         else:
#             c= ",".join(map(str, col))
#             print c
#         if len(row)==0:
#             # print "Empty set " + "("+ str((format(abs(timeit.timeit() - start),'.2f')))+" sec)"
#             sys.exit()
#         if len(row)>1:
#             for rows in row:
#                 r = ",".join(map(str, rows))
#                 print r
#         else:
#             if len(row)==1 and isinstance(row[0], list) :
#                 row = row[0]
#             r = ",".join(map(str, row))
#             print r
#         # print length + " rows in set " + "("+ str((format(abs(timeit.timeit() - start),'.2f')))+" sec)"
#
#
#     except Exception as e:
#         print e
#         sys.exit("ERROR: PRINT RESULT ERROR")

def printResult(col,row):
    try:
        result = PrettyTable(col)
        length = str(len(row))
        if len(row)==0:
            print "Empty set " + "("+ str((format(abs(timeit.timeit() - start),'.2f')))+" sec)"
            sys.exit()
        if len(row)>1:
            for rows in row:
                result.add_row(rows)
        else:
            if len(row)==1 and isinstance(row[0], list) :


                row = row[0]
            result.add_row(row)
        result.align = "r"
        print result
        print length + " rows in set " + "("+ str((format(abs(timeit.timeit() - start),'.2f')))+" sec)"
    except Exception as e:
        print e
        sys.exit("ERROR: PRINT RESULT ERROR")
