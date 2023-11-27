import pandas as pd

# Load the data into a DataFrame
df = pd.read_csv("/Users/vennilasooben/ift3700_tp-3/csv_rawdata/21.List_of_sovereign_states_and_dependencies_by_total_fertility_rate/21.2 table.csv")
print(df.columns)
# Select only the desired columns
selected_columns = ['Country', 'Total Fertility rate in 2021 (births/woman)']
df = df[selected_columns]

# Clean the "Country" column
df['Country/'] = df['Country'].str.replace(r'[^A-Za-z0-9\s]+', '', regex=True)


df['Total Fertility rate in 2021 (births/woman)'] = pd.to_numeric(df['Total Fertility rate in 2021 (births/woman)'], errors='coerce')


# Save the cleaned data to a new CSV file
df.to_csv('21.2 cleaned.csv', index=False)