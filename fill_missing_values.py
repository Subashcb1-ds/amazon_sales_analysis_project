import pandas as pd

# Load the CSV file
file_path = "C:/Users/Subashcb1/Downloads/Corrected_Amazon_Sale_Report - Sheet1.csv"
df = pd.read_csv(file_path)

# Fill blank cells in the "Courier Status" column with "Pending"
df['Courier Status'].fillna('Unknown', inplace=True)

# Save the updated DataFrame back to a new CSV file or overwrite the existing one
output_file_path = "C:/Users/Subashcb1/Downloads/Updated_Amazon_Sale_Report.csv"
df.to_csv(output_file_path, index=False)

print("Blank cells in the 'Courier Status' column have been filled with 'Pending'.")
