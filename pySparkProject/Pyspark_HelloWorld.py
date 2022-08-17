from pandas.core.algorithms import isin

from pyspark.sql import SparkSession
from pyspark import SparkConf,SparkContext
import pandas as pd

from pyspark.sql import functions as f
from pyspark.sql.functions import col

conf = SparkConf()
'''
spark=SparkSession.builder. \
    config("spark.hadoop.hive.exec.dynamic.partition", "true") \
    .config("spark.hadoop.hive.exec.dynamic.partition.mode", "nonstrict") \
    .enableHiveSupport().appName("spark app").master("local[*]").getOrCreate()
'''


spark=SparkSession.builder.enableHiveSupport().appName("spark app").master("local[*]").getOrCreate()

spark.sparkContext.setLogLevel("WARN")
'''*******Word count by creating RDD******'''
input_rdd=spark.sparkContext.textFile("inputs\data.csv")
print(input_rdd.getNumPartitions())
cnt=input_rdd.mapPartitions(lambda it: [sum(1 for _ in it)])
# print(cnt.collect())
# input2=spark.read.csv("C:\\Users\\PRADEEP\\Downloads\\tx.csv\\fl.csv")
wordcount=input_rdd.flatMap(lambda x:x.split(',')).map(lambda x:(x,1)).reduceByKey(lambda a,b:a+b)
print(wordcount.collect())
''' *******Creating DF'''
input=spark.read.option("header",True).csv("C:\\Users\\PRADEEP\\Downloads\\tx.csv\\tx.csv")

inp=input.limit(20)
input.show()
inp.show()
''' ****** Select...where'''
# input1=input.select(input["STREET"],input["LAT"],input["HASH"]).where(input["STREET"]=='ACR 117')
input1=input.where(input["STREET"]=='ACR 117')
input2=input.select(input.LAT,input.STREET,input.NUMBER).where((input.STREET=='ACR 117') & (input.NUMBER!='0'))
input3=input.select(input["LAT"],input["STREET"],input["HASH"]).where((input["STREET"]=='ACR 117') & (input["NUMBER"]=='0'))
input4=input.select(col("LAT")).where(col("STREET")=='ACR 117')
input5=input.select(f.col("LAT")).where(f.col("STREET")=='ACR 117')
input5_2=input.select(f.col("STREET")).filter(f.col("STREET").isin('ACR 117','ACR 2265','REDTOWN')).orderBy(col('STREET'),ascending=False)
print(input2.show(2,False))
print(input3.show(2,False))
print(input4.show(2,False))
print(input5.show(2,False))
print(input5_2.show(100,False))
print("------FLTER DF--------- \n")

'''********Spark merge 2 datasets******'''

# uniondf=input3.unionAll(input2)
uniondf=input3.union(input2)
print(uniondf.show())

''' When...otherwise in pyspark '''

input6=input.withColumn('New_calc_col',f.when(col('STREET').rlike('ACR'),f.lit('PRADEEP')).otherwise(f.lit("Bangalore")))
print(input6.show(10,False))
input7=input6.limit(10)
print(input7.show(10,False))
''' ******* Saving DF to a hive table***'''
# input6.coalesce(2).write.partitionBy("New_calc_col").mode("append").saveAsTable('table1') #hive table
# input6.coalesce(2).write.insertInto('table1') #hive table insert if exists
input7.coalesce(1).write.mode("append").partitionBy("New_calc_col").saveAsTable("Table") #works as append table toreinserting the data in same table
# input6.coalesce(2).write.partitionBy("New_calc_col").mode("append").csv('outputs/results') #as file

outputdf=spark.read.parquet(r"spark-warehouse\table")
print("******Reading from parquet warehouse table *****")
print(outputdf.show(1000,False))
# print(input1.show())


# convering sparkDF to pandas DF
# pd_df=input1.toPandas()
# print(pd_df.describe())
print(input.rdd.getNumPartitions())
print(spark.sparkContext.getConf().get("spark.sql.files.minPartitionNum"))
# input2.show(100)
