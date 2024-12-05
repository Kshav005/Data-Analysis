import pandas as pd

# Step 1: Import data from two Excel files into two DataFrames
df1 = pd.read_excel('workshop1.xlsx')
df2 = pd.read_excel('workshop2.xlsx')


# a. Merging of the two data frames to find the names of students who had attended both workshops
print("\n=== Step a ===")
common_students = pd.merge(df1[['Name']], df2[['Name']], on='Name', how='inner').drop_duplicates()
print("Students who attended both workshops:\n", common_students)

# b. Find names of all students who have attended a single workshop only
print("\n=== Step b ===")
students_only1 = pd.concat([df1[['Name']], df2[['Name']]]).drop_duplicates(keep=False)
print("Students who attended only one workshop:\n", students_only1)

# c. Merge two data frames row-wise and find the total number of records in the data frame
print("\n=== Step c ===")
df_rowwise = pd.concat([df1, df2], axis=0)
total_records = len(df_rowwise)
print("Total number of records after row-wise merge:", total_records)

# d. Merge two data frames row-wise and use two columns viz. names and dates as multi-row indexes.
# Generate descriptive statistics for this hierarchical data frame.
print("\n=== Step d ===")
df_hierarchical = df_rowwise.set_index(['Name', 'Date'])
print("Hierarchical DataFrame (Name, Date as multi-index):\n", df_hierarchical.head())

# Generating descriptive statistics for the hierarchical data frame
statistics = df_hierarchical.describe()
print("\nDescriptive statistics for the hierarchical data frame:\n", statistics)
