import sqlite3
import pandas as pd

conn = sqlite3.connect('test_database')
c = conn.cursor()
#
# c.execute('''
#           CREATE TABLE IF NOT EXISTS products
#           ([product_id] INTEGER PRIMARY KEY, [product_name] TEXT, [price] INTEGER)
#           ''')
#
# c.execute('''
#           INSERT INTO products (product_id, product_name, price)
#
#                 VALUES
#                 (1,'Computer',800),
#                 (2,'Printer',200),
#                 (3,'Tablet',300),
#                 (4,'Desk',450),
#                 (5,'Chair',150)
#           ''')
#
# conn.commit()
#

# Reading data from table and creating DF


conn = sqlite3.connect('test_database')

sql_query = pd.read_sql_query('''
                               SELECT
                               *
                               FROM products
                               ''', conn)

df = pd.DataFrame(sql_query, columns=['product_id', 'product_name', 'price'])
print(df)