import pypyodbc
import pyodbc
import pandas as pd
from sqlalchemy.engine import URL
from sqlalchemy import create_engine
from sqlalchemy.types import Integer,NVARCHAR
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
print(df['id'].count())
print("DF before new column:\n",df)
#dynamically adding a column:
for i in range(0,df['id'].count()):
    if (i%2==0):
        print(i)
        df.loc[[i],'address'] = 'Bangalore'
        df.loc[[i], 'id2'] = df['id']*100
    else:
        df.loc[[i],'address'] = 'Delhi'
        df.loc[[i], 'id2'] = df['id'] * 100

print(df.dtypes)
df=df.astype({"id2":int})
print(df.dtypes)
print(df)

#*******to insert the data frame in sql
# df.to_sql("fruit",engine)
#*******to insert the data frame in sql without mentioning the data type#####

# df.to_sql('Inventory', con=engine, if_exists='append',index=False)

#******to specify the data type######

# df.to_sql('Inventory', con=engine, if_exists='append',index=False,
#                                                       dtype={"id": Integer(),
#                                                              "name":NVARCHAR(),
#                                                              "quantity": Integer()})
# print(engine.execute("SELECT * FROM dbo.Inventory").fetchall())

