import time

from pyspark.sql import SparkSession
from pyspark import SparkConf,SparkContext
# import pandas as pd
from pyspark.sql import functions as f
from pyspark.sql.functions import col
spark=SparkSession.builder.enableHiveSupport().appName("spark app").master("local[*]").getOrCreate()

spark.sparkContext.setLogLevel("WARN")
conf = SparkConf()
# df=spark.read.csv(r"C:\Users\PRADEEP\PycharmProjects\My_Project\pySparkProject\inputs\data.csv")
df=spark.read.csv('s3://pyspark-pradeep-stepfunction\data.csv')
print(df.show(100,False))
df.write.csv('s3://pyspark-pradeep-stepfunction/output/')
