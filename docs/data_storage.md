# Data storage for milestone 1

## Choice
We use **Google Cloud Storage (GCS)** as our cloud storage for the dataset.

Reason: GCS is object storage and is ideal for raw datasets and ML artifacts (models, reports). It also satisfies the course requirement to avoid local storage.

## GCS location
- Bucket: gs://<YOUR_BUCKET_NAME>/
- Dataset object: gs://<YOUR_BUCKET_NAME>/data/raw/Housing.csv

## Note
The dataset is not stored in Git and is uploaded to the cloud.