from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.conf import SparkConf

sc = SparkContext(master="local", appName="Spark Demo")

print(SparkConf().getAll())

