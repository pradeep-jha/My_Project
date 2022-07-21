import datetime

from pyspark import SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, col, input_file_name, lit
import json
import random
import requests
conf=SparkConf()
#https://www.youtube.com/watch?v=Q_pN8OFjXr4
url='https://api.publicapis.org/entries'
def read_webapi_data(url):
    response=requests.get(url)
    responsejson=response.json()
    return response.text,responsejson

outresult,outresultjson=read_webapi_data(url)
with open('C:\\Users\\PRADEEP\\PycharmProjects\\First_Project\\pySparkProject\\outputs\\outresult.json', 'w') as f:
            f.write(outresult)
            f.close()


spark=SparkSession.builder.appName("pyspark-read_api").master("local[*]").getOrCreate()
api_data=spark.read.option('multiline',True).\
    json('C:\\Users\\PRADEEP\\PycharmProjects\\First_Project\\pySparkProject\\outputs\\outresult.json')
api_data.show()
api_data.printSchema()

publicapi_df=api_data.select('count',explode('entries').alias('entries_data'))
publicapi_df.printSchema()
publicapi_df.show(10,False)

finaldf=publicapi_df.select('count','entries_data.API','entries_data.Auth','entries_data.Category','entries_data.Cors',
                            'entries_data.Description','entries_data.HTTPS','entries_data.Link')
finaldf.printSchema()
finaldf.show(10,True)
finald_d=finaldf.withColumn('Modified_datetime',lit(datetime.datetime.now())).withColumn('file_name',lit(input_file_name()))
outfile_postfix="spark-webdata_out"+str(random.randint(1,10000))
finald_d.show()
finald_d.write.option("header",True).csv('C:\\Users\\PRADEEP\\PycharmProjects\\First_Project\\pySparkProject\\outputs\\'+outfile_postfix)