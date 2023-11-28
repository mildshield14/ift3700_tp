import pandas as pd

# Load the CSV file into a DataFrame
csv_file_path = '/Users/vennilasooben/Downloads/ift3700_tp/cleaning_whole_data/final_table.csv'
df = pd.read_csv(csv_file_path)

# Extract the first column with names
names_column = df.iloc[:, 0]

# Create a dictionary to store data based on the first letter
data_by_first_letter = {}
for name in names_column:
    first_letter = name[0].upper()
    if first_letter not in data_by_first_letter:
        data_by_first_letter[first_letter] = []
    data_by_first_letter[first_letter].append(name)

# Create a new DataFrame based on the dictionary
new_df = pd.DataFrame(data_by_first_letter.items(), columns=['First Letter', 'Names'])

# Save the new DataFrame to a CSV file
new_csv_file_path = 'organized_data_country_names.csv'
new_df.to_csv(new_csv_file_path, index=False)

print(f"Data has been organized and saved to {new_csv_file_path}.")
