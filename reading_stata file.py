import pandas as pd

# Define the file path
file_path = '/Users/mizq7/Desktop/RESEARCH/_MANUSCRIPT/UNDER PREPARATION/Democracy Paper/Data_democracy.dta/muinul.democracy.dta'

# Load the .dta file into a pandas DataFrame
df = pd.read_stata(file_path)

# Display the first few rows of the DataFrame
print(df.head())

# Display basic information about the data
print(df.info())

#Converting .dta data to excel file
# Import pandas
import pandas as pd

# Save the DataFrame to an Excel file
output_file_path = '/Users/mizq7/Desktop/RESEARCH/Exported_Dataset.xlsx'

# Export the dataset to an Excel file
df.to_excel(output_file_path, index=False)

print(f"Dataset has been successfully exported to {output_file_path}")

