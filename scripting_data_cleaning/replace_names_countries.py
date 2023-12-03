import os
import pandas as pd

def process_folder(folder_path, replace_this, replace_with):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".csv"):
                file_path = os.path.join(root, file)
                df = pd.read_csv(file_path)

                if "Country" in df.columns:
                    # Replace the specified string in the "Country" column
                    df["Country"] = df["Country"].str.replace(replace_this, replace_with)

                    # Save the modified DataFrame back to the same file
                    df.to_csv(file_path, index=False)

def main():
    folder_path = "/Users/vennilasooben/Downloads/ift3700_tp/csv_duplicated_columns"
    replace_this = input("replacw what?")
    replace_with = input("replace with what?")
    
    process_folder(folder_path, replace_this, replace_with)

if __name__ == "__main__":
    main()
