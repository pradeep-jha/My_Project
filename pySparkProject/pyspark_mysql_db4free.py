import random
from pyspark.sql import SparkSession
from pyspark import SparkConf,SparkContext
from pyspark.sql import functions
from pyspark.sql import DataFrameWriter
import datetime

print(datetime.date.today())
print(datetime.datetime.now())

from pyspark.sql.functions import lit

conf = SparkConf()

spark=SparkSession.builder.appName("spark app").master("local[*]").\
    config("spark.driver.extraClassPath","C:\\Users\\PRADEEP\\PycharmProjects\\First_Project\\pySparkProject\\mysql-connector-j-8.0.32.jar").\
    config("spark.sql.parquet.compression.codec","gzip").\
    getOrCreate()
#

# df = spark.read.format("jdbc").option("url","jdbc:mysql://localhost/<database_name>").option("driver","com.mysql.jdbc.Driver").option("dbtable","<table_name>").option("user","<user>").option("password","<password>").load()


print(spark.version)
print(spark.sparkContext.getConf().get(("spark.sql.parquet.compression.codec")))
# spark.sparkContext.setLogLevel("WARN")

#****** set variable to be used to connect the database *****
database = "TestDB"
table = "test"
user = "admin_db4free"
password  = "admin1234"
qry="select * from test"
print(qry)
# read table data into a spark dataframe
jdbcDF = spark.read.format("jdbc") \
    .option("url", f"jdbc:mysql://www.db4free.net:3306/testdb2023") \
    .option("dbtable", '({sql}) as src'.format(sql=qry)) \
    .option("user", user) \
    .option("password", password) \
    .option("driver", "com.mysql.cj.jdbc.Driver") \
    .load()

# show the data loaded into dataframe
jdbcDF.show()
input2=jdbcDF.withColumnRenamed("name","input_name").withColumn("modified_date",lit(datetime.date.today())).withColumn("modified_datetime",lit(datetime.datetime.now()))
# finaldf=input2.join(jdbcDF,["id"],"inner")
input2.printSchema()
input2.show(100,False)



# Write to MySQL Table
input2.write \
  .format("jdbc") \
  .option("driver","com.mysql.cj.jdbc.Driver") \
  .option("url", "jdbc:mysql://www.db4free.net:3306/testdb2023") \
  .option("dbtable", "employee") \
  .option("user", user) \
  .option("password", password) \
  .option("driver", "com.mysql.cj.jdbc.Driver") \
  .save()