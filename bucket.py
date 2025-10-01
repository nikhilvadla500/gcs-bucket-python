from google.cloud import storage

# Path to your service account JSON
key_path = r"C:/Users/Nikhil kumar/Downloads/norse-strata-465507-a6-a8005c0cee8e.json"

# Initialize client using service account
storage_client = storage.Client.from_service_account_json(key_path)

project_id = "norse-strata-465507-a6"
bucket_name = "nikhil-bucket-12345"  # must be globally unique

# Create bucket
new_bucket = storage_client.create_bucket(bucket_name, project=project_id, location="US")
print(f" Bucket {new_bucket.name} created in project {project_id}.")
