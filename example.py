import pandas as pd
import os 

# Read data from JSON file
json_file = 'data.json'  # Replace 'data.json' with the path to your JSON file
data = pd.read_json(json_file)

# Write data to Excel file (XLSX format)
excel_file = 'data.xlsx'  # Output Excel file name
data.to_excel(excel_file, index=False)

print(f"Data has been successfully converted and saved to '{excel_file}' file.")