# 1. Write a Python script to upload a file to Google Cloud Storage using the `google-cloud-storage` library.
# ANSWER HERE
from google.cloud import storage
# Path to service account JSON
key_path = r"C:\Users\Nikhil kumar\Downloads\norse-strata-465507-a6-a8005c0cee8e.json"
storage_client = storage.Client.from_service_account_json(key_path)
project_id = "norse-strata-465507-a6"
bucket_name = "nikhil-bucket-12345"   # must already exist in GCP
source_file_path = r"C:\Users\Nikhil kumar\Downloads\gke.txt"
destination_blob_name = "gke.txt"
bucket = storage_client.bucket(bucket_name)
blob = bucket.blob(destination_blob_name)
blob.upload_from_filename(source_file_path)
print(f"File {source_file_path} uploaded to bucket {bucket_name} as {destination_blob_name}.")
