from functools import reduce

from pyspark.sql import SparkSession
from pyspark.sql import functions as f
from pyspark.sql.functions import *
from pyspark.sql.types import *

spark=SparkSession.builder.appName("bulk_col_rename").master("local").getOrCreate()
df1=spark.read.option('HEADER',True).option('inferschema',True).csv("inputs/data2.csv")
print(df1.printSchema())
print(df1.show())
cols=df1.columns
# x="A"
# print(x+"def")
# df2=reduce(lambda new_df,i:new_df.withColumnRenamed(i,i.replace("c","d")),cols,df1) #--for replacing some charcter in col name
df2=reduce(lambda new_df,i:new_df.withColumnRenamed(i,(i+"_New")),cols,df1)
print(df2.show())


'''
list2=['A','B','C',1]
print(*list2)
def fun(x,y):
    res=str(x)+str(y)
    return res
res1=reduce(fun,list2)
print(res1)
'''
'''***Method-2***'''
def col_rename(df,c):
    newdf=df.withColumnRenamed(c,(c+"new"))
    return newdf
df3=reduce(col_rename,cols,df1)
print(df3.show())


#####***Creating Surrogate Key pyspark****#####

df4=df2.withColumn("Surrogate_Key",monotonically_increasing_id()+100)
print(df4.show())
print(df4.printSchema())
