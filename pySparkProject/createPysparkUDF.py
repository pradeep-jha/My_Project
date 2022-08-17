from time import monotonic

from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col, input_file_name
import findspark

from pyspark.sql.types import StringType

findspark.init()
print(findspark.find())
spark=SparkSession.builder.config("spark.master", "local[4]").appName("PysparkUDF").master("local[*]").getOrCreate()

df=spark.read.option("header",True).option("delimiter",",").csv("inputs/input.csv")
# df=spark.read.option("header","true")\
#                 .option("mergeSchema", "true").parquet("outputs\\result322017.187")

print(df.rdd.getNumPartitions())
print(spark.sparkContext.getConf().get("spark.sql.files.minPartitionNum"))
df.repartition(4)
print(df.rdd.getNumPartitions())

print(df.show(truncate=False))


def myfunc(col_name):
    res=str(col_name).strip().upper()+"_UDF"
    return(res)

myfunc_udf=udf(lambda x:myfunc(x))

df2=df.withColumn('name_upper',myfunc_udf("name"))
print(df2.show())

""" Using UDF on SQL --we need to register it first for using in sql query"""
spark.udf.register("myfuncUDF", myfunc,StringType())

df.registerTempTable("table1")
sqldf=spark.sql("select id,name,myfuncUDF(name) as new_name from table1")
sqldf.show()
print(sqldf.count())
randomval=monotonic()
# creating multiple partition:

print(sqldf.rdd.getNumPartitions())
print(spark.sparkContext.getConf().getAll())

'''Partition By is used for writing data on disk in  partitioned columns'''

# sqldf.write.partitionBy("name").option("header",True).parquet(r"outputs\result"+str(randomval))
df.repartition(4).write.option("header",True).csv(r"outputs\result"+str(randomval))
'''*****reading Partitioned data from partitioned columns in spark DF   ****'''

df_part=spark.read.option("header","true")\
                .option("mergeSchema", "true").parquet("outputs\\result322017.187")
# df_part=spark.read.option("header","true")\
#                 .option("mergeSchema", "true").csv("outputs\\result318704.031")
print(df_part.rdd.getNumPartitions())
print(spark.sparkContext.getConf().getAll())
df_part1=df_part.withColumn('file',input_file_name())
print(df_part1.count())
print(df_part1.show(truncate=False))