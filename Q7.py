import pandas as pd

# Create the data frame
data = {
    'FamilyName': ['Shah', 'Vats', 'Vats', 'Kumar', 'Vats', 'Kumar', 'Shah', 'Shah', 'Kumar', 'Vats'],
    'Gender': ['Male', 'Male', 'Female', 'Female', 'Female', 'Male', 'Male', 'Female', 'Female', 'Male'],
    'MonthlyIncome': [44000.00, 65000.00, 43150.00, 66500.00, 255000.00, 103000.00, 55000.00, 112400.00, 81030.00, 71900.00]
}

df = pd.DataFrame(data)

# a. Calculate and display familywise gross monthly income
print("\n=== Step a: Familywise Gross Monthly Income ===")
familywise_income = df.groupby('FamilyName')['MonthlyIncome'].sum()
print(familywise_income)

# b. Display the highest and lowest monthly income for each family name
print("\n=== Step b: Highest and Lowest Monthly Income for Each Family ===")
income_stats = df.groupby('FamilyName')['MonthlyIncome'].agg(['max', 'min'])
print(income_stats)

# c. Calculate and display monthly income of all members earning income less than Rs. 80000.00
print("\n=== Step c: Members Earning Less than Rs. 80000.00 ===")
low_income_members = df[df['MonthlyIncome'] < 80000]
print(low_income_members)

# d. Display total number of females along with their average monthly income
print("\n=== Step d: Total Number of Females and Their Average Monthly Income ===")
females = df[df['Gender'] == 'Female']
total_females = females.shape[0]
avg_income_females = females['MonthlyIncome'].mean()
print(f"Total number of females: {total_females}")
print(f"Average monthly income of females: Rs. {avg_income_females:.2f}")

# e. Delete rows with Monthly income less than the average income of all members
print("\n=== Step e: Rows with Monthly Income Less Than the Average Income ===")
average_income = df['MonthlyIncome'].mean()
df_above_avg = df[df['MonthlyIncome'] >= average_income]
print(f"Average income of all members: Rs. {average_income:.2f}")
print(df_above_avg)
