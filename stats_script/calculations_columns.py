import os
import re
import pandas as pd

def process_folder(folder_path, output_file):
    all_data = pd.DataFrame(columns=["Country"])

    variance=["Variance"]
    minimum=["Minimum"]
    mode=["Mode"]
    maximum=["Maximum"]
    mean=["Mean"]
    median=["Median"]
    column_name=["Stats"]

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if "cleaned.csv" in file:
                file_path = os.path.join(root, file)
                df = pd.read_csv(file_path)

                if "Country" in df.columns:
                   
                    column_name.append(df.columns[1])

                    second_column_data = df.iloc[:, 1]

                    # Convert the column to numeric values
                    numeric_values = pd.to_numeric(second_column_data, errors='coerce')

                    # Filter out NaN values
                    numeric_values = numeric_values.dropna()

                    # Calculate statistics
                    variance.append(round(numeric_values.var(),3))
                    maximum.append(round(numeric_values.max(),3))
                    minimum.append(round(numeric_values.min(),3))
                    mean.append(round(numeric_values.mean(),3))
                    median.append(round(numeric_values.median(),3))
                    mode.append(numeric_values.mode().values[0] if not numeric_values.empty else None)

    dataa=[]              
 
    dataa.append(variance)
    dataa.append(maximum)
    dataa.append(minimum)
    dataa.append(mean)
    dataa.append(median)
    dataa.append(mode)
    all_data = pd.DataFrame(dataa, columns=column_name)
    all_data.to_csv(output_file, index=False)

def main():
    folder_path = "/Users/vennilasooben/Downloads/ift3700_tp/csv_duplicated_columns"
    output_file = "/Users/vennilasooben/Downloads/ift3700_tp/csv_statistics/csv_stats_columns.csv" 
    process_folder(folder_path, output_file)


    # Read the CSV file into a DataFrame
    df = pd.read_csv(output_file)

    # Sort the columns based on the numbers in parentheses
    sorted_columns =  sorted(df.columns[1:], key=extract_number_from_column)

    # Reorganize the DataFrame columns
    df = df[["Stats"] + sorted_columns]

    # Save the resulting DataFrame to a CSV file
    df.to_csv(output_file, index=False)


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
    main()