
from pyspark.sql import SparkSession
from pkg_pyspark import properties

#inp=sc.textFile("C:\\Users\\pradeep\\Desktop\pycharm_spark\\input\\Titanic_header.txt")
#words=inp.flatMap(lambda x: x.split('\t')).map(lambda x: (x,1)).reduceByKey(lambda x,y: x+y)
#words.foreach(print)
input_path=properties.input ##parametarised input path
#SparkConf().getAll()
spark = SparkSession \
            .builder \
            .getOrCreate()

# .master("local[*]") \  #commenting to use config in ony spark context..it should be before getorcreate()
#inp=spark.read.format('csv').options(header=True,inferSchema=True).option("delimiter", "\t").load("C:\\Users\\pradeep\\Desktop\pycharm_spark\\input\\Titanic.txt")
inp=spark.read.format('csv').options(header=True,inferSchema=True).option("delimiter", "\t").load(input_path)

inp.createOrReplaceTempView("titanic")
res=spark.sql("select * from titanic")
res.show(100,False)
spark.stop()