import pandas as pd
import numpy as np

df = pd.read_csv("path/to/your/iris.csv")

#Basic overview
print("First 5 rows of the dataset:")
print(df.head())

print("\nShape of the dataset:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

print("\nDescriptive statistics:")
print(df.describe())

print("\nMean of each numeric column (NumPy):")
print(np.mean(df.select_dtypes(include=np.number), axis=0))

print("\nStandard deviation (NumPy):")
print(np.std(df.select_dtypes(include=np.number), axis=0))

print("\nCorrelation matrix (Pandas):")
print(df.corr(numeric_only=True))

print("\nUnique:")
print(df['species'].unique())

print("\nValue counts:")
print(df['element'].value_counts())

# Plots

