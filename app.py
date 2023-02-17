import re
from google.cloud import storage
storage_client = storage.Client()

uri = "gs://chimbuc-playground-tf/networking/sandbox/default.tfstate"
matches = re.match("gs://(.*?)/(.*)", uri)
if matches:
    bucket, object_name = matches.groups()
    print(bucket)
    print(object_name)
    bucket = storage_client.get_bucket(bucket)
    blob = bucket.blob(object_name)

    with blob.open("r") as f:
        print(f.readlines())
