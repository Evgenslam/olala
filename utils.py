import pandas as pd

"""
Pandas function
"""
# Replace 'input_file.xlsx' with your actual XLSX file
input_file = 'Karelia.xlsx'

# Load the Excel file into a pandas DataFrame
df = pd.read_excel(input_file)

# Replace 'output_file.csv' with the desired name for the CSV file
output_file = 'Karelia_Suoyarvi.csv'

# Write the DataFrame to a CSV file with semicolon delimiter
df.to_csv(output_file, sep=';', index=False)


