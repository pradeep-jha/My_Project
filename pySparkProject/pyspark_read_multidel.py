import os
from time import monotonic

import dbutils as dbutils

from pyspark.sql import SparkSession
from pyspark.sql import functions as f
from pyspark import SparkConf
from pyspark.sql.functions import col
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, FloatType, DateType

print(os.getcwd())

spark=SparkSession.builder.appName("multidel").master('local[*]').getOrCreate()
print(spark.version)
df1=spark.read.option('header',True).option('delimiter','||').csv('inputs\multi_del.csv',sep='||')


df2=spark.read.option('header',True).option('delimiter',',').csv('inputs\multi_sep.csv')
df3=df2.withColumn("Subject1",f.split(col("marks"),"[|]")[0]).withColumn("Subject2",f.split(col("marks"),"[|]")[1]).\
        withColumn("Subject3",f.split(col("marks"),"[|]")[2]).withColumn("Subject3",f.split(col("marks"),"[|]")[3]).drop("marks")

print(df1.show(100,False))

print(df2.show(100,False))
print(df3.show())
# *****to print default functions available in Pyspark
# print(spark.sql("SHOW Functions").show(1000,truncate=False))

#To join 2 DF's

joindf=df1.alias("t1").join(df3.alias("t2"),df1["id"]==df3["id"],"inner")
print(joindf.show(100,False))
# **accessing columns from different DF
specific_col_df=joindf.selectExpr("t1.id","t2.name","Subject1*10 as new_subject")
print(specific_col_df.show(100,False))

# **lit function for assiging a hardcoded value

agg_df=joindf.withColumn("sub1",f.lit("Subject1"))

#**Aggregating the column values,To change the datatype fisrt add another column by "withcolumn" and then cast it to int

agg_df=joindf.withColumn("sub1",f.col("Subject1").cast('int')).withColumn("sub2",f.col("Subject2").cast('int')).groupby("t1.id").\
              sum("sub1","sub2")
print(agg_df.show())
print(agg_df.printSchema())

#**changing the data types in data frame using structtype.


schema=StructType([StructField("id",IntegerType(),True),
                   StructField("Name",StringType(),True),
                   StructField("Address",StringType(),True),
                   StructField("Price",FloatType(),True),
                   StructField("date",DateType(),True)

                   ])

df4=spark.read.option('delimiter',',').csv('inputs/data.csv',schema=schema)
print(df4.printSchema())
print(df4.show(100,False))
agg_df4=df4.groupby("date","id").avg("price").orderBy("date",ascending=False)
print(agg_df4.show())
randomval=monotonic()
agg_df4.write.option("header",True).csv(r"outputs\result"+str(randomval))