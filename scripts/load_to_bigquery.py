import os
from google.cloud import bigquery
from google.cloud import storage
import yaml


def load_files_to_bigquery():
    with open("config/config.yaml", "r") as file:
        config = yaml.safe_load(file)

    client = bigquery.Client()
    storage_client = storage.Client()

    bucket = storage_client.get_bucket(config["gcs_bucket"])
    blobs = bucket.list_blobs(prefix=config["gcs_folder"])

    for blob in blobs:
        if blob.name.endswith(".csv") or blob.name.endswith(".parquet"):
            table_id = f"{config['bigquery_project']}.{config['bigquery_dataset']}.{os.path.splitext(blob.name)[0]}"
            table_ref = client.dataset(config["bigquery_dataset"]).table(
                os.path.splitext(blob.name)[0]
            )

            try:
                client.get_table(table_ref)
                load_job = client.load_table_from_uri(
                    f"gs://{config['gcs_bucket']}/{blob.name}",
                    table_id,
                    job_config=bigquery.LoadJobConfig(
                        source_format=(
                            bigquery.SourceFormat.CSV
                            if blob.name.endswith(".csv")
                            else bigquery.SourceFormat.PARQUET
                        ),
                        autodetect=True,
                        write_disposition=bigquery.WriteDisposition.WRITE_APPEND,
                    ),
                )
            except bigquery.NotFound:
                load_job = client.load_table_from_uri(
                    f"gs://{config['gcs_bucket']}/{blob.name}",
                    table_id,
                    job_config=bigquery.LoadJobConfig(
                        source_format=(
                            bigquery.SourceFormat.CSV
                            if blob.name.endswith(".csv")
                            else bigquery.SourceFormat.PARQUET
                        ),
                        autodetect=True,
                        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
                    ),
                )
            load_job.result()
            print(f"Loaded {blob.name} into {table_id}")


if __name__ == "__main__":
    load_files_to_bigquery()
