from pyspark.sql import SparkSession
import pandas as pd
import datetime as dt
from pyspark.sql import functions as f
from pyspark.sql import Column as col
from pyspark.sql import types as t
from pyspark.sql.functions import from_unixtime, unix_timestamp
from pyspark.sql.types import StructType, StructField, DoubleType, StringType, IntegerType, TimestampType

spark = SparkSession.builder.master("local[*]") \
    .appName("Excle_Spark") \
    .getOrCreate()
in_df = pd.read_excel("C:\\Users\\pradeep\\Desktop\\pycharm_spark\\input\\911-2.xlsx", sheet_name='Sheet3',
                      converters={'Date': str})
# pd.set_option("display.max_rows", 100, "display.max_columns", 100)
# print(tabulate(in_df, headers='keys', tablefmt='psql'))
print(dt.datetime.fromtimestamp(1449769200))
#########in_df['epoch'] = (in_df['timeStamp'] - dt.datetime(1970,1,1)).dt.total_seconds()
##########in_df['epoch'] = in_df['epoch'].astype('Int64')

# print(in_df.to_string())
# print(in_df,False)
# print(in_df['epoch'])

print(in_df.dtypes)

schema = StructType([StructField("lat", DoubleType(), True), StructField("lng", DoubleType(), True),
                     StructField("desc", StringType(), True) \
                        , StructField("zip", StringType(), True), StructField("title", StringType(), True), \
                     StructField('timestamp_col', t.LongType(), True), StructField("twp", StringType(), True), \
                     StructField("addr", StringType(), True), StructField("e", IntegerType(), True)
                     ])

sdf = spark.createDataFrame(in_df, schema=schema)
sdf.printSchema()
# =sdf_dt_convrtd=sdf.withColumn("aaa",sdf.col('zip').cast("integer"))
sdf_dt_convrtd = sdf.withColumn("Timestamp", from_unixtime(sdf["timestamp_col"], "dd-MM-yyyy HH:mm:ss"))
sdf_dt_convrtd.printSchema()
sdf.show(100, False)
sdf_dt_convrtd.show(100, False)
'''
in_df=spark.read.format("com.crealytics.spark.excel") \
                .option("location", "C:\\Users\\pradeep\\Desktop\\pycharm_spark\\input\\911.xlsx") \
                .option("useHeader", "true") \
                .option("treatEmptyValuesAsNulls", "false") \
                .option("inferSchema", "false") \
                .option("addColorColumns", "false") \
                .option("dataAddress", "sheet1!") \
                .load("C:\\Users\\pradeep\\Desktop\\pycharm_spark\\input\\911.xlsx")

in_df.show(10,False)
'''
