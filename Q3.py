import pandas as pd
import numpy as np

# Step 1: Create a DataFrame with 50 rows and 3 columns of random numeric data
df = pd.DataFrame(np.random.rand(50, 3))

# Step 2: Randomly assign NaN values in 5 locations
for i in range(5):
    x, y = np.random.randint(0, 50), np.random.randint(0, 3)
    df.iloc[x, y] = pd.NA
    print(f"NaN inserted at position ({x}, {y})")

# a. Identify and count missing values in a data frame
print("\n=== Step a ===")
print("Total missing values in the DataFrame:", df.isnull().sum().sum())
print("Missing values per column:\n", df.isnull().sum())

# b. Drop the column having more than 5 null values
print("\n=== Step b ===")
df_cleaned = df.dropna(thresh=len(df)-5, axis=1)
print("DataFrame after dropping columns with more than 5 NaN values:\n", df_cleaned)

# c. Identify the row label having maximum sum and drop that row
print("\n=== Step c ===")
max_sum_row = df_cleaned.sum(axis=1).idxmax()  # Find row with the maximum sum
df_cleaned = df_cleaned.drop(max_sum_row)
print(f"DataFrame after dropping the row with the highest sum (Row {max_sum_row}):\n", df_cleaned)

# d. Sort the DataFrame on the basis of the first column (column 0)
print("\n=== Step d ===")
df_sorted = df_cleaned.sort_values(by=0)
print("DataFrame sorted by the first column (0):\n", df_sorted)

# e. Remove all duplicates from the first column
print("\n=== Step e ===")
df_unique = df_sorted.drop_duplicates(subset=0)
print("DataFrame after removing duplicates from the first column:\n", df_unique)

# f. Find the correlation between the first and second column and the covariance between second and third column
print("\n=== Step f ===")
correlation_0_1 = df_unique[0].corr(df_unique[1])
covariance_1_2 = df_unique[1].cov(df_unique[2])
print(f"Correlation between column 0 and 1: {correlation_0_1}")
print(f"Covariance between column 1 and 2: {covariance_1_2}")

# g. Discretize the second column and create 5 bins
print("\n=== Step g ===")
df_unique = df_unique.dropna(subset=[1])
df_unique['1_bins'] = pd.cut(df_unique[1], bins=5)
print("DataFrame with second column discretized into 5 bins:\n", df_unique[[1, '1_bins']])
