import boto3

s3=boto3.client("s3")
print(s3)
# upload_file(file_name, bucket, object_name=None):
s3.upload_file('Data/test_python-s3_file_upload.txt','mypython-s3-bucket','test_python-s3_file_upload.txt')
print("upload successful!!")