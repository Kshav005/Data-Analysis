import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load Titanic dataset
df = sns.load_dataset('titanic')

# a. Clean the data by dropping the column which has the largest number of missing values
print("\n=== Step a ===")
missing_vals = df.isnull().sum()
print("Missing values in each column:\n", missing_vals)

# Drop the column with the most missing values
column_to_drop = missing_vals.idxmax()
df_cleaned = df.drop(columns=[column_to_drop])
print(f"Column dropped: {column_to_drop}")
print(df_cleaned.head())

# b. Find total number of passengers with age more than 30
print("\n=== Step b ===")
passengers_above_30 = df[df['age'] > 30].shape[0]
print(f"Total passengers with age more than 30: {passengers_above_30}")

# c. Find total fare paid by passengers of second class
print("\n=== Step c ===")
total_fare_second_class = df[df['pclass'] == 2]['fare'].sum()
print(f"Total fare paid by passengers of second class: {total_fare_second_class}")

# d. Compare number of survivors of each passenger class
print("\n=== Step d ===")
survivors_by_class = df.groupby('pclass')['survived'].sum()
print("Number of survivors by passenger class:\n", survivors_by_class)

# e. Compute descriptive statistics for age attribute gender wise
print("\n=== Step e ===")
age_gender_stats = df.groupby('sex')['age'].describe()
print("Descriptive statistics for age gender wise:\n", age_gender_stats)

# f. Draw a scatter plot for passenger fare paid by Female and Male passengers separately
print("\n=== Step f ===")
plt.figure(figsize=(8, 6))
sns.scatterplot(x='fare', y='age', hue='sex', data=df)
plt.title('Scatter Plot: Fare Paid by Female and Male Passengers')
plt.xlabel('Fare Paid')
plt.ylabel('Age')
plt.show()

# g. Compare density distribution for features age and passenger fare
print("\n=== Step g ===")
plt.figure(figsize=(8, 6))
sns.kdeplot(df['age'].dropna(), label='Age', shade=True)
sns.kdeplot(df['fare'].dropna(), label='Fare', shade=True)
plt.title('Density Distribution for Age and Fare')
plt.legend()
plt.show()

# h. Draw a pie chart for three groups labeled as class 1, class 2, class 3 respectively
print("\n=== Step h ===")
pclass_counts = df['pclass'].value_counts()
pclass_percentage = pclass_counts / pclass_counts.sum() * 100

plt.figure(figsize=(8, 6))
plt.pie(pclass_percentage, labels=['Class 1', 'Class 2', 'Class 3'], autopct='%1.1f%%', colors=['#ff9999','#66b3ff','#99ff99'])
plt.title('Passenger Class Distribution')
plt.show()

# i. Find % of survived passengers for each class and answer the question “Did class play a role in survival?”
print("\n=== Step i ===")
survival_rate_by_class = df.groupby('pclass')['survived'].mean() * 100
print(f"Percentage of survived passengers by class:\n{survival_rate_by_class}")

# Did class play a role in survival?
if survival_rate_by_class[1] > survival_rate_by_class[3]:
    print("\nYes, class played a role in survival. Higher class passengers had a higher survival rate.")
else:
    print("\nNo, class did not play a significant role in survival.")
