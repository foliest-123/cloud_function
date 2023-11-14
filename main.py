from pathlib import Path
from google.cloud import storage

def upload_files_to_gcs(bucket_name, source_folder):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    
    source_folder_path = Path(source_folder)
    my_files = [file for file in source_folder_path.iterdir() if file.is_file()]

    for file_path in my_files:
        filename = file_path.name
        destination_blob_name = filename
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(str(file_path))

        print(f"{filename} uploaded to blob as {destination_blob_name}.")


bucket_name = "json_file_folder"
source_folder = r"./json_data"
upload_files_to_gcs(bucket_name, source_folder)

