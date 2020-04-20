from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.conf import SparkConf
sc = SparkContext(master="local",appName="Spark Demo")
# inp=sc.textFile("C:\\Users\\pradeep\\Desktop\pycharm_spark\\input\\Titanic_header.txt")
#words=inp.flatMap(lambda x: x.split('\t')).map(lambda x: (x,1)).reduceByKey(lambda x,y: x+y)
#words.foreach(print)
SparkConf().getAll()
spark = SparkSession \
            .builder \
            .appName("wordcount") \
            .master("local[*]") \
            .getOrCreate()
inp=spark.read.format('text').options(header=True,inferSchema=True).load("C:\\Users\\pradeep\\Desktop\pycharm_spark\\input\\Titanic.txt")
inp.createOrReplaceTempView("titanic")
res=spark.sql("select * from titanic")
res.show(100,False)
