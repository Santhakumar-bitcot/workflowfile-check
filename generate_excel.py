import pandas as pd

# Sample data
data = {
    'Name': ['John', 'Jane', 'Doe'],
    'Age': [28, 34, 29],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Write the DataFrame to an Excel file
excel_path = 'output.xlsx'
df.to_excel(excel_path, index=False)

print(f"Excel file generated at: {excel_path}")
