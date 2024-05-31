import os
from google.cloud import bigquery
from google.cloud import storage
import yaml

def load_files_to_bigquery():
    with open('config/config.yaml', 'r') as file:
        config = yaml.safe_load(file)

    client = bigquery.Client()
    storage_client = storage.Client()

    bucket = storage_client.get_bucket(config['gcs_bucket'])
    blobs = bucket.list_blobs(prefix=config['gcs_folder'])

    for blob in blobs:
        if blob.name.endswith('.csv'):
            table_id = f"{config['bigquery_project']}.{config['bigquery_dataset']}.{os.path.splitext(blob.name)[0]}"
            load_job = client.load_table_from_uri(
                f"gs://{config['gcs_bucket']}/{blob.name}",
                table_id,
                job_config=bigquery.LoadJobConfig(
                    source_format=bigquery.SourceFormat.CSV,
                    autodetect=True,
                ),
            )
        elif blob.name.endswith('.parquet'):
            table_id = f"{config['bigquery_project']}.{config['bigquery_dataset']}.{os.path.splitext(blob.name)[0]}"
            load_job = client.load_table_from_uri(
                f"gs://{config['gcs_bucket']}/{blob.name}",
                table_id,
                job_config=bigquery.LoadJobConfig(
                    source_format=bigquery.SourceFormat.PARQUET,
                    autodetect=True,
                ),
            )
        load_job.result()
        print(f"Loaded {blob.name} into {table_id}")

if __name__ == "__main__":
    load_files_to_bigquery()
