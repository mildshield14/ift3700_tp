import os
import csv

def remove_spaces(file):
    with open(file, 'r', newline='', encoding='utf-8') as csv_in:
        reader = csv.reader(csv_in)
        rows = [','.join(field.strip() for field in row) for row in reader]

    with open(file, 'w', newline='', encoding='utf-8') as csv_out:
        csv_out.write('\n'.join(rows))

if __name__ == "__main__":
    remove_spaces("/Users/vennilasooben/Downloads/ift3700_tp/csv_duplicated_columns/28.List_of_countries_by_population_growth_rate/28.1 cleaned.csv")
