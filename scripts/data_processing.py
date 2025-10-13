import pandas as pd
import numpy as np
import boto3
import os

def generate_data():
    data = pd.DataFrame({
        'ID': np.arange(1, 11),
        'Value': np.random.randint(1, 100, 10)
    })

    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "data.csv")

    data.to_csv(output_file, index=False)
    print("✅ Data saved to:", output_file)
    print(data)

    # Upload to S3
    upload_to_s3(output_file, "data-pipeline-bucket-raajveer-01", "data.csv")

def upload_to_s3(file_path, bucket_name, s3_key):
    s3 = boto3.client('s3')
    try:
        s3.upload_file(file_path, bucket_name, s3_key)
        print(f"✅ File uploaded to S3: s3://{bucket_name}/{s3_key}")
    except Exception as e:
        print(f"❌ Failed to upload to S3: {e}")

if __name__ == "__main__":
    generate_data()

