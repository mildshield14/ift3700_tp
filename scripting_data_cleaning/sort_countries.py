import os
import pandas as pd
import re

def process_folder(folder_path, output_file):
    all_data = pd.DataFrame(columns=["Country"])

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if "cleaned.csv" in file:
                file_path = os.path.join(root, file)
                df = pd.read_csv(file_path)

                if "Country" in df.columns:
                    # Extract the "Country" and the second column data
                    country_column = df["Country"]
                    second_column_label = df.columns[1]  
                    second_column_data = df.iloc[:, 1]

                    # Create a DataFrame with "Country" and the second column data
                    result_df = pd.DataFrame({"Country": country_column, f"{second_column_label}": second_column_data})

                    # Merge with the existing data using "Country" as the key
                    all_data = pd.merge(all_data, result_df, on="Country", how="outer")

    all_data.to_csv(output_file, index=False)

# Function to extract the number from the column names
def extract_number_from_column(column_name):
        try:
            #asked chatgpt about regex to extract (number) from second columns name and got that answer
          numbers = re.findall(r'\((\d+)\)', column_name)
          return tuple(map(int, numbers))
        except ValueError:
         print("put (number) in youe column header for example: Intentional Homicide Rate(4)")
         return float('inf')   # If no number is found, place it at the end for now temporarily

if __name__ == "__main__":

    folder_path = "/Users/vennilasooben/Downloads/ift3700_tp/csv_duplicated_columns"
    output_file = "/Users/vennilasooben/Downloads/ift3700_tp/cleaning_whole_data/final_table.csv"
    process_folder(folder_path, output_file)

    # Read the CSV file into a DataFrame
    df = pd.read_csv(output_file)

    # Sort the columns based on the numbers in parentheses
    sorted_columns =  sorted(df.columns[1:], key=extract_number_from_column)

    # Reorganize the DataFrame columns
    df = df[["Country"] + sorted_columns]

    # Save the resulting DataFrame to a CSV file
    df.to_csv(output_file, index=False)

