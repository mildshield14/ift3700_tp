import pandas as pd

# Load the data into a DataFrame
df = pd.read_csv("/Users/vennilasooben/Downloads/ift3700_tp/csv_duplicated_columns/9.Importance_of_religion_by_country/9.1 cleaned.csv")
print(df.columns)
# Select only the desired columns
selected_columns = ['Country', 'Importance of Religion(9)']
df = df[selected_columns]

# Clean the "Country" column
df['Country'] = df['Country'].str.replace(r'[^A-Za-z0-9\s]+', '', regex=True)

df['Importance of Religion(9)'] = df['Importance of Religion(9)'].str.replace('%', '')
df['Importance of Religion(9)'] = pd.to_numeric(df['Importance of Religion(9)'], errors='coerce')

# Save the cleaned data to a new CSV file
df.to_csv('9.1 cleaned.csv', index=False)