# Megatron-MiniSQL-Engine
Mini sql engine which run a subset of SQL Queries using ​command line interface

Type of Query Supported:
1.Select all records
2.Aggregate functions
3.Select/project with distinct from one table
4.Project Columns from multiple tables
5.Select with where from one or more tables
6.Projection of one or more(including all the columns) from two tables with one join condition




How to run program:
./20172046 "query"

Examples:
Query1:
./20172046 "select * from table1"

+----------+----------+----------+
| table1.a | table1.b | table1.c |
+----------+----------+----------+
|      922 |      158 |     5727 |
|      640 |      773 |     5058 |
|      775 |       85 |    10164 |
|     -551 |      811 |     1534 |
|     -952 |      311 |     1318 |
|     -354 |      646 |     7063 |
|     -497 |      335 |     4549 |
|      411 |      803 |    10519 |
|     -900 |      718 |     9020 |
|      858 |      731 |     3668 |
|      640 |      773 |    51058 |
+----------+----------+----------+
11 rows in set (0.00 sec)

Query2:
./20172046 "select A,G from table1,table3 where table1.A > table3.G and table1.B < table3.E"
+----------+----------+
| table1.a | table3.g |
+----------+----------+
|      922 |       85 |
|      640 |      158 |
|      640 |       85 |
|      640 |      311 |
|      640 |      335 |
|      411 |      158 |
|      411 |       85 |
|      411 |      311 |
|      411 |      335 |
|      858 |      158 |
|      858 |       85 |
|      858 |      311 |
+----------+----------+
12 rows in set (0.00 sec)
