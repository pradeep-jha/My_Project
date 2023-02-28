from pyspark.sql import SparkSession
from pyspark.sql import functions as f
from pyspark.sql.functions import *
from pyspark.sql.types import *

spark=SparkSession.builder.appName("Column_manipulation").master("local").getOrCreate()
col_name=['col1','col2','col3','col4','col5']
print("*****Printing Data Type of col_name****")
print(type(col_name))
df1=spark.read.csv("inputs/data.csv")
print(df1.show())
print(df1.columns)
print(df1.printSchema())
df1_1=df1.toDF(*col_name)
print("Adding Header to DF1 dynamically")
print(df1_1.printSchema())
print(df1_1.show())
df2=df1.toDF('col1','col2','col3','col4','col5')
print(df2.printSchema())
print(df2.show())

# ***to validate the column order in two DF****
a=df2.columns
print(a)
print(type(a))
print(df2.dtypes)
if (col_name==a):
       print("matching")
try:
       assert col_name==a ,"Schema not matching"
except Exception as e:
       print(str(e))



''' ***Changing datatypes in existing DF'''
df3=df2.withColumn('col1',f.col('COL1').cast(IntegerType())).withColumn('col4',f.col('col4').cast(DoubleType())) \
       .withColumn('col5',f.col('col5').cast(DateType()))
print(df3.printSchema())
print(df3.show())
df4=df3.withColumn('DateTime',f.current_timestamp())
print(df4.printSchema())
print(df4.show(truncate=False))
'''**Date conversion'''
df5=df4.withColumn('New_Date1',f.date_format(col('DateTime'),"dd-MM-yyyy")) \
       .withColumn('New_Date2',f.date_format(col('DateTime'),"dd-MMM-yyyy")) \
       .withColumn('New_Date3',f.date_format(col('DateTime'),"dd/MM/yyyy")) \
       .withColumn('New_Date4',f.date_format(col('DateTime'),"yyyy-MM-dd")) \
       .withColumn('quarter',f.quarter(col('DateTime'))) \
       .withColumn('year',f.year(col('DateTime'))) \
       .withColumn('month',f.month(col('DateTime'))) \
       .withColumn('date',f.dayofmonth(col('DateTime'))) \
       .withColumn('weekofyear',f.weekofyear(col('DateTime')))


print(df5.printSchema())
print(df5.show(truncate=False))