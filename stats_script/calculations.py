import pandas as pd
import os
import matplotlib.pyplot as plt

def calculate_statistics(csv_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)

    statistics_text =""

    # Loop through all columns in the DataFrame
    for column in df.columns:
        # Convert the column to numeric values
        numeric_values = pd.to_numeric(df[column], errors='coerce')

        # Filter out NaN values
        numeric_values = numeric_values.dropna()

        # Calculate statistics
        moyenne = numeric_values.mean()
        mediane = numeric_values.median()
        maximum = numeric_values.max()
        mode_value = numeric_values.mode().values[0] if not numeric_values.empty else None
        minimum = numeric_values.min()
        variance_value = numeric_values.var()

        # Append statistics to the string
        statistics_text += (
            f"Column: {column}\n"
            f"Moyenne: {moyenne}\n"
            f"Médiane: {mediane}\n"
            f"Maximum: {maximum}\n"
            f"Mode: {mode_value}\n"
            f"Minimum: {minimum}\n"
            f"Variance: {variance_value}\n"
            f"\n"
        )

        # Select the second column for the histogram
        column_to_plot = df.iloc[:, 1] 

        # Plot the histogram
        plt.hist(column_to_plot, bins=20, color='blue', edgecolor='black')

        # Add labels and title
        plt.xlabel('Values')
        plt.ylabel('Frequency')
        plt.title('Histogram of Second Column')

        # Show the plot
        plt.show()

        print("done")


    return statistics_text

print(calculate_statistics(input("Input csv absolute path")))