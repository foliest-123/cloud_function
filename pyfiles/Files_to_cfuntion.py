import functions_framework
from google.cloud import storage
import requests
from pathlib import Path

@functions_framework.http
def send_file():

# https://us-central1-vijay-project-01.cloudfunctions.net/function-2
    url = 'https://us-central1-vijay-project-01.cloudfunctions.net/function-2'
    directory = Path(r'C:\cloud_function_files\json_data')
    number_of_files = sum(1 for item in directory.iterdir() if item.is_file())
    for i in range(number_of_files):
        file_path =fr'C:\cloud_function_files\json_data\file_{i+1}.ndjson'  
        headers = {'Content-Type': 'application/ndjson'} 
        with open(file_path, 'rb') as file:
            files = {'newfile': file} 
    
            response = requests.post(url, files=files) 
        if response.status_code == 200:
            print('File successfully uploaded!')
            print(response.text)
        else:
            print('Failed to upload file. Status code:', response.status_code)

























    # bucket_name = "json_file_folder"
    # storage_client = storage.Client()
    # bucket = storage_client.get_bucket(bucket_name)
    
    # # Get the uploaded JSON file from the request
    # uploaded_file =requests.files.get('newfile')

        
    # # Upload the JSON file to Google Cloud Storage
    # blob = bucket.blob(uploaded_file)
    # blob.upload_from_filename(temp_file_path)
    
    # return f"File '{uploaded_file}' uploaded to GCS"



send_file()


# def upload_files_http():
#     bucket_name = "json_file_folder"
#     storage_client = storage.Client()
#     bucket = storage_client.get_bucket(bucket_name)
    
#     # Get the uploaded JSON file from the request
#     uploaded_file = request.files.get('file')

#     if uploaded_file and uploaded_file.filename.endswith('.ndjson'):
        
#         # Upload the JSON file to Google Cloud Storage
#         blob = bucket.blob(uploaded_file.filename)
#         blob.upload_from_filename(temp_file_path)
        
#         return f"File '{uploaded_file.filename}' uploaded to GCS"

#     return "No JSON file uploaded or file format is incorrect"
