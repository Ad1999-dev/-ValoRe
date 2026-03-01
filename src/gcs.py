from google.cloud import storage


def create_bucket(project_id, bucket_name, location="europe-west1"):
    """Create a new GCS bucket."""
    client = storage.Client(project=project_id)
    bucket = client.bucket(bucket_name)
    new_bucket = client.create_bucket(bucket, location=location)
    print(f"Bucket created: {new_bucket.name} (location: {new_bucket.location})")


def upload_to_gcs(project_id, bucket_name, source_file_path, destination_blob_name):
    """Upload a local file to GCS."""
    client = storage.Client(project=project_id)
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_path)
    print(f"Uploaded: {source_file_path} -> gs://{bucket_name}/{destination_blob_name}")


def list_blobs(project_id, bucket_name, prefix=None):
    """List files in a bucket (optionally filtered by prefix)."""
    client = storage.Client(project=project_id)
    blobs = client.list_blobs(bucket_name, prefix=prefix)

    print(f"Listing gs://{bucket_name}/{prefix or ''}")
    for blob in blobs:
        print(blob.name)


def download_from_gcs(project_id, bucket_name, source_blob_name, destination_file_path):
    """Download a file from GCS to local disk."""
    client = storage.Client(project=project_id)
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)

    blob.download_to_filename(destination_file_path)
    print(f"Downloaded: gs://{bucket_name}/{source_blob_name} -> {destination_file_path}")


if __name__ == "__main__":
    # Fill these in
    PROJECT_ID = "valore-mlsd-project"
    BUCKET_NAME = "mlsd-valore-2026-0001"
    LOCATION = "europe-west1"

    # Local dataset path (NOT tracked in git)
    LOCAL_CSV = r"./data/raw/Housing.csv"

    # Where to store in bucket
    DEST_BLOB = "data/raw/Housing.csv"

    # Step 1: create bucket
    # create_bucket(PROJECT_ID, BUCKET_NAME, LOCATION)

    # Step 2: upload dataset
    # upload_to_gcs(PROJECT_ID, BUCKET_NAME, LOCAL_CSV, DEST_BLOB)

    # Step 3: list bucket contents
    # list_blobs(PROJECT_ID, BUCKET_NAME, prefix="data/")

    # Step 4: download back (optional verification)
    # download_from_gcs(PROJECT_ID, BUCKET_NAME, DEST_BLOB, "Housing_downloaded.csv")