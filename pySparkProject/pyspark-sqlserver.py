import random

from pyspark.sql import SparkSession
from pyspark import SparkConf,SparkContext
from pyspark.sql import DataFrameWriter
import datetime

conf = SparkConf()

spark=SparkSession.builder.appName("spark app").master("local[*]").\
    config("spark.driver.extraClassPath","C:\\Users\\PRADEEP\\PycharmProjects\\First_Project\\pySparkProject\\sqljdbc42.jar").\
    getOrCreate()
print(spark.version)
spark.sparkContext.setLogLevel("WARN")
input=spark.read.option('delimiter','\t').option('header',True).csv("C:\\Users\\PRADEEP\\PycharmProjects\\First_Project\\pySparkProject\\inputs\\input.csv")
# input2=spark.read.csv("C:\\Users\\PRADEEP\\Downloads\\tx.csv\\fl.csv")
input.show()
# set variable to be used to connect the database
database = "TestDB"
table = "dbo.Inventory"
user = "sa"
password  = "pradeep@123"
qry="select * from dbo.Inventory"
print(qry)
# read table data into a spark dataframe
jdbcDF = spark.read.format("jdbc") \
    .option("url", f"jdbc:sqlserver://20.214.145.105:1433;databaseName={database};") \
    .option("dbtable", '({sql}) as src'.format(sql=qry)) \
    .option("user", user) \
    .option("password", password) \
    .option("driver", "com.microsoft.sqlserver.jdbc.SQLServerDriver") \
    .load()

# show the data loaded into dataframe
jdbcDF.show()
input2=input.withColumnRenamed("name","input_name")
joindf=input2.join(jdbcDF,["id"],"inner")
joindf.show()


datetime_object = datetime.datetime.now()
print(datetime_object)
out_file="result"+str(random.randint(1,10000))
print(out_file)
print(spark.sparkContext.defaultParallelism)
print(spark.sparkContext.defaultMinPartitions)
print(joindf.rdd.getNumPartitions())
print(input2.rdd.getNumPartitions())
print(jdbcDF.rdd.getNumPartitions())
joindf.coalesce(1).write.parquet("C:\\Users\\PRADEEP\\PycharmProjects\\First_Project\\pySparkProject\\outputs\\"+out_file)
