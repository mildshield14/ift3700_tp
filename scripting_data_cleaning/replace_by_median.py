import pandas as pd
from sklearn.impute import SimpleImputer

df = pd.read_csv('/Users/vennilasooben/ift3700_tp-3/csv_duplicated_columns/28.List_of_countries_by_population_growth_rate/28.1 extracted.csv')

# Identify numeric columns
numeric_columns = df.select_dtypes(include=['number']).columns

# Calculate median for each numeric column
medians = df[numeric_columns].median()

# Impute missing values with themedian
imputer = SimpleImputer(strategy='constant', fill_value=round(medians[0],3))
df[numeric_columns] = imputer.fit_transform(df[numeric_columns])

# Save the DataFrame with imputed value
df.to_csv('/Users/vennilasooben/ift3700_tp-3/csv_duplicated_columns/28.List_of_countries_by_population_growth_rate/28.1 cleaned.csv', index=False)
