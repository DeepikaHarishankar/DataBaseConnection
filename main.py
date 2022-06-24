# ---- DATABASE TABLE COMPARISON AND WRITING A MISMATCH REPORT IN CSV FORMAT ------------------#

# TODO 1  IMPORT STATEMENTS

from database_connection import DatabaseConnection
from compare import Compare

# TODO 2 INSTANTIATE DATABASECONNECTION CLASS AND ACCESS DATA FROM EXTERNAL TABLE AND INTERNAL TABLE
connection = DatabaseConnection()
table_1 = connection.external_products
table_2 = connection.internal_products

# TODO 3 INSTANTIATE COMPARE CLASS AND CALL ON THE COMPARE METHOD. PASS ON THE DATA FROM TWO TABLES
#  THAT NEEDS TO BE COMPARED

compare = Compare(table_1, table_2)
compare.compare_table()
