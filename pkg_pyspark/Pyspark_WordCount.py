from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.conf import SparkConf

sc = SparkContext(master="local", appName="Spark Demo")
inp = sc.textFile("C:\\Users\\pradeep\\Desktop\pycharm_spark\\input\\Titanic_header.txt")
SparkConf().getAll()
'''
spark = SparkSession \
            .builder \
            .getOrCreate()
inp=spark.read.text("C:\\Users\\pradeep\\Desktop\pycharm_spark\\input\\Titanic.txt")
'''
''' test '''
words = inp.flatMap(lambda x: x.split('\t')).map(lambda x: (x, 1)).reduceByKey(lambda x, y: x + y)
words.foreach(print)
