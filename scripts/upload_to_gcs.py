import os
from google.cloud import storage
import yaml

def upload_files_to_gcs():
    with open('config/config.yaml', 'r') as file:
        config = yaml.safe_load(file)

    client = storage.Client()
    bucket = client.get_bucket(config['gcs_bucket'])

    for root, _, files in os.walk(config['data_folder']):
        for file in files:
            if file.endswith('.csv') or file.endswith('.parquet'):
                local_path = os.path.join(root, file)
                blob = bucket.blob(f"{config['gcs_folder']}/{file}")
                blob.upload_from_filename(local_path)
                print(f"Uploaded {file} to {config['gcs_bucket']}/{config['gcs_folder']}")

if __name__ == "__main__":
    upload_files_to_gcs()
