import boto3

BUCKET_NAME = "olist-ecommerce-pipeline-dotun-2026"

FILE_PATH = r"C:\Users\ajayi\Documents\Brazilian E-commerce Dataset\Data\Processed\olist_orders_transformed.csv"

OBJECT_NAME = "olist_orders_transformed.csv"

s3 = boto3.client("s3")

s3.upload_file(FILE_PATH, BUCKET_NAME, OBJECT_NAME)

print("Upload to Amazon S3 successful!")