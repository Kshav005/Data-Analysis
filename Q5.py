import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import datasets

# a. Load the Iris data into a pandas DataFrame
iris = datasets.load_iris()
df = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])
df['target'] = iris['target']
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# Check the data
print(df.head())

# Use pandas.info() to check data types
print("\n=== Step a ===")
df.info()

# b. Find the number of missing values in each column
print("\n=== Step b ===")
missing_values = df.isnull().sum()
print("Missing values in each column:\n", missing_values)

# c. Plot bar chart to show the frequency of each class label in the data
print("\n=== Step c ===")
plt.figure(figsize=(8, 6))
sns.countplot(x='species', data=df)
plt.title('Frequency of Each Class Label (Species)')
plt.xlabel('Species')
plt.ylabel('Frequency')
plt.show()

# d. Scatter plot for Petal Length vs Sepal Length and fit a regression line
print("\n=== Step d ===")
plt.figure(figsize=(8, 6))
sns.regplot(x=df['sepal length (cm)'], y=df['petal length (cm)'])
plt.title('Scatter Plot: Petal Length vs Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.show()

# e. Plot density distribution for Petal width
print("\n=== Step e ===")
plt.figure(figsize=(8, 6))
sns.kdeplot(df['petal width (cm)'], shade=True)
plt.title('Density Distribution for Petal Width')
plt.xlabel('Petal Width (cm)')
plt.show()

# f. Use a pair plot to show pairwise bivariate distribution in the Iris Dataset
print("\n=== Step f ===")
sns.pairplot(df, hue='species', markers=["o", "s", "D"])
plt.show()

# g. Draw heatmap for any two numeric attributes
print("\n=== Step g ===")
plt.figure(figsize=(8, 6))
corr_matrix = df[['sepal length (cm)', 'petal length (cm)']].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Heatmap for Sepal Length and Petal Length')
plt.show()

# h. Compute mean, mode, median, standard deviation, standard error for each numeric feature
print("\n=== Step h ===")

# Compute statistics for each column
numeric_cols = df.select_dtypes(include=[np.number]).columns[:-1]

for col in numeric_cols:
    mean = df[col].mean()
    mode = df[col].mode()[0]
    median = df[col].median()
    std_dev = df[col].std()
    sem = df[col].sem()  # Standard error of the mean

    print(f"Statistics for {col}:")
    print(f"Mean: {mean}")
    print(f"Mode: {mode}")
    print(f"Median: {median}")
    print(f"Standard Deviation: {std_dev}")
    print(f"Standard Error: {sem}")
    print()

# i. Compute correlation coefficients between each pair of features and plot heatmap
print("\n=== Step i ===")
plt.figure(figsize=(10, 8))
correlation_matrix = df.iloc[:, :4].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='viridis')
plt.title('Correlation Heatmap of Features')
plt.show()
