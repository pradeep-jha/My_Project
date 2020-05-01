from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.conf import SparkConf
#sc = SparkContext(master="local",appName="Spark Demo") # commeenting to call from main .only one sc should be there
'''inp=sc.textFile("C:\\Users\\pradeep\\Desktop\pycharm_spark\\input\\Titanic_header.txt")
SparkConf().getAll() '''
spark = SparkSession \
            .builder \
            .appName("wordcount") \
            .master("local[*]") \
            .getOrCreate()
inp=spark.read.format('csv').options(header=True,inferSchema=True).option("delimiter", "\t").load("C:\\Users\\pradeep\\Desktop\pycharm_spark\\input\\Titanic.txt").toDF('1','2','3','4','5','6','7','8','9','10','11','12')
'''words=inp.flatMap(lambda x: x.split('\t')).map(lambda x: (x,1)).reduceByKey(lambda x,y: x+y)
words.foreach(print)'''
inp.printSchema()
inp.show(2,False)
inp.withColumn('ID',inp['1']).show(1,False)# use of withcolumn
inp.select('1','4').show(5,False)#use of select

spark.stop()