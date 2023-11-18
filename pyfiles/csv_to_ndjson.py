import csv
import pandas as pd
import math
import ndjson 
import json
 # Import the ndjson module

# file_count = 1
# count = 0

# df = pd.read_csv('./csv/amazon.csv')
# jsonfile_base = './json_data/file_'

# length = len(df)
# rowcount = 50
# runtime = math.ceil(length / rowcount)
# df['discounted_price'] =df['discounted_price'].convert_dtypes()
# print(df.size)

file_path = r'C:\cloud_function_files\json_data\file_16.ndjson'
with open(file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        try:
            json_obj = json.loads(line)
            for key, value in json_obj.items():
                print(f"Key: {key}, Value Type: {type(value)}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON at line {line_number}: {e}")
            print(f"Problematic line content: {line.strip()}")
        break


# for i in range(runtime):
#     start_index = i * rowcount
#     end_index = min((i + 1) * rowcount, length)
#     fifty_values = df[start_index:end_index]
#     fifty_values_dict = fifty_values.to_dict('records')
#     print(fifty_values_dict)
#     jsonfile = f'{jsonfile_base}{i + 1}.ndjson'  # Change the file extension to ".ndjson"
#     with open(jsonfile, 'w') as json_file_object:
#         ndjson.dump(fifty_values_dict, json_file_object) 

