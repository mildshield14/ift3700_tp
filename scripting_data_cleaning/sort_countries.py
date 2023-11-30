import os
import pandas as pd

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

def main():
    folder_path = "/Users/gabrielhazan/Documents/GitHub/ift3700_tp/csv_duplicated_columns"
    output_file = "/Users/gabrielhazan/Documents/GitHub/ift3700_tp/cleaning_whole_data/final_table.csv"
    process_folder(folder_path, output_file)

if __name__ == "__main__":
    main()
