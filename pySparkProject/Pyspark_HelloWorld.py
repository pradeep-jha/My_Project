from pyspark.sql import SparkSession
from pyspark import SparkConf,SparkContext

conf = SparkConf()

spark=SparkSession.builder.appName("spark app").master("local[*]").getOrCreate()


spark.sparkContext.setLogLevel("WARN")

input=spark.read.csv("C:\\Users\\PRADEEP\\Downloads\\tx.csv\\tx.csv")
# input2=spark.read.csv("C:\\Users\\PRADEEP\\Downloads\\tx.csv\\fl.csv")



input.show()
# input2.show(100)