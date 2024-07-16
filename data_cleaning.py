import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = r"C:\Users\Subashcb1\Downloads\Amazon Sale Report (1).xlsx"
df = pd.read_excel(file_path)

# Define the mappings
mappings = {
    'Category': {'kurta': 'Kurta'},
    'ship-state': {
        'APO': 'ANDHRA PRADESH',
        'AR': 'ARUNACHAL PRADESH',
        'DADRA AND NAGAR': 'DADRA AND NAGAR HAVELI AND DAMAN AND DIU',
        'NL': 'NAGALAND',
        'ODISHA': 'ODISHA',
        'orissa': 'ODISHA',
        'PB': 'PUNJAB',
        'Punjab/Mohali/Zirakpur': 'PUNJAB',
        'TRIPURA': 'TRIPURA',
        'RJ': 'RAJASTHAN',
        'Rajsthan': 'RAJASTHAN',
        'Rajshthan': 'RAJASTHAN',
        'Gujarat': 'GUJARAT',
        'Pondicherry': 'PUDUCHERRY',
    }
}

# Apply the mappings to the DataFrame
for column, mapping in mappings.items():
    if column in df.columns:
        df[column] = df[column].replace(mapping)

# Ensure all state names in 'ship-state' are in uppercase
if 'ship-state' in df.columns:
    df['ship-state'] = df['ship-state'].str.upper()

# Sales Analysis
total_sales_by_category = df.groupby('Category')['Amount'].sum().sort_values(ascending=False)
top_5_categories = total_sales_by_category.head(5)
print("Top 5 Categories by Sales Amount:")
print(top_5_categories)

# Fulfillment Analysis
fulfillment_counts = df['fulfilled-by'].value_counts(normalize=True) * 100
print("Fulfillment Method Distribution:")
print(fulfillment_counts)

# Geographical Analysis
total_sales_by_state = df.groupby('ship-state')['Amount'].sum().sort_values(ascending=False)
top_5_states = total_sales_by_state.head(5)
print("Top 5 States by Sales Amount:")
print(top_5_states)

# Visualize Top 5 Categories by Sales Amount
top_5_categories.plot(kind='bar', title='Top 5 Categories by Sales Amount')
plt.xlabel('Category')
plt.ylabel('Total Sales Amount')
plt.show()
