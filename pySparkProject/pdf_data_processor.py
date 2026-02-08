from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType
from pyspark.sql.functions import split, col,concat
import pdfplumber
from PyPDF2 import PdfReader
pdf_file = "C:\\Users\\PRADEEP\\Downloads\\sample_employee_data.pdf"
# Initialize a Spark session
spark = SparkSession.builder \
    .appName("Process Employee Data from PDF") \
    .getOrCreate()

def pdf_to_text(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Extract text from the PDF
text_data = pdf_to_text(pdf_file)

# Convert the extracted text to a list of rows
lines = text_data.split("\n")

# Skip the first two rows
lines = lines[2:]
print(lines)

# Create an RDD from the lines
rdd = spark.sparkContext.parallelize(lines)

# Split the lines into columns (assuming space-separated values)
# Adjust the delimiter if necessary
rdd_split = rdd.map(lambda line: line.split())

# Convert the RDD to a DataFrame
columns = ["Employee ID", "FName","LName", "Department", "Position", "Salary"]  # Adjust column names as per your data
df = rdd_split.toDF(columns)
df.show()
# Separate the first and last names from the FullName column
df_cleaned = df.withColumn("Name",concat(col("FName"),col("LName"))).drop("FName").drop("LName")

# Show the cleaned DataFrame
df_cleaned.show()
csv_output_path='outputs\\result.csv'
# Write the cleaned DataFrame to a CSV file
df_cleaned.repartition(1).write.csv(csv_output_path, header=True)

# Stop the Spark session
spark.stop()