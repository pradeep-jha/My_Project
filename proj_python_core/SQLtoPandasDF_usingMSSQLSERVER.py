import pypyodbc
import pyodbc
import pandas as pd
from sqlalchemy.engine import URL
from sqlalchemy import create_engine
database = "TestDB"
table = "dbo.Inventory"
user = "sa"
password  = "pradeep@123"
server="20.214.145.105,1433"
qry="select * from dbo.Inventory"
driver="ODBC Driver 17 for SQL Server"
# cnxn = pypyodbc.connect("Driver={SQL Server Native Client 11.0};"
#                         "Server=server_name;"
#                         "Database=database;"
#                         "uid=user;pwd=password")

# cnxn = pyodbc.connect(driver='{SQL Server}', host=server, database=database,
#                        user=user, password=password)
#
# print(cnxn)

connection_string = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={user};PWD={password}"
connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})


engine = create_engine(connection_url)
df = pd.read_sql_query(qry, engine)

print(df)