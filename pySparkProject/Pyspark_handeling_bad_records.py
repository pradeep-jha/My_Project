from pyspark.sql import SparkSession
from pyspark.sql.functions import input_file_name
from pyspark.sql.types import *

spark=SparkSession.builder.appName('Pyspark_badrecord_handling').getOrCreate()
# Running sql directly on file
df_sql=spark.sql("select * from csv.`C:\\Users\\PRADEEP\\PycharmProjects\\First_Project\\pySparkProject\\inputs\\data_badrec.csv`")
df_sql.show(100,False)
df=spark.read.option("mode","PERMISSIVE").option("inferschema",True).option("header",True).csv(r"C:\Users\PRADEEP\PycharmProjects\First_Project\pySparkProject\inputs\data_badrec.csv")
df.show(100,False)

df1=spark.read.option("mode","DROPMALFORMED").option("inferschema",True).option("header",True).csv(r"C:\Users\PRADEEP\PycharmProjects\First_Project\pySparkProject\inputs\data_badrec.csv")
df1.show(100,False)

# df2=spark.read.option("mode","FAILFAST").option("inferschema",True).option("header",True).csv(r"C:\Users\PRADEEP\PycharmProjects\First_Project\pySparkProject\inputs\data_badrec.csv")
# df2.show(100,False)

# ***To get the corrupt record in a seperate column and process other records
# /**Defining a new schema using Struct Type and struct filed
df_schema=StructType([StructField('ID',IntegerType(),True),
                    StructField('Name',StringType(),True),
                    StructField('Address',StringType(),True),
                      StructField('AirQuality',DoubleType(),True),
                      StructField('Date',DateType(),True),
                      StructField('_CorruptRecord',StringType(),True)
                      ])

df3=spark.read.option("mode","PERMISSIVE")\
    .schema(df_schema)\
    .option("columnNameOfCorruptRecord","_CorruptRecord")\
    .option("inferschema",True)\
    .option("header",True)\
    .csv(r"C:\Users\PRADEEP\PycharmProjects\First_Project\pySparkProject\inputs\data_badrec.csv")
df3.show(100,False)

df4=df3.withColumn("FileName",input_file_name())
df4.show(100,False)
