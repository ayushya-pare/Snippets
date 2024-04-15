#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import pandas as pd
import numpy as np

def analyze_dataframe(df):

    # Display basic information about the DataFrame
    print("DataFrame Info:")
    df.info()
    
    # Show columns and their data types
    print("\nColumns and Data Types:")
    print(df.dtypes)
    
    # Check if the first column is an index
    if df.columns[0] == df.index.name:
        print("\nThe first column is the index.")
    else:
        print("\nThe first column is not the index, it is:", df.columns[0])
    
    # Show unique values in each column
    print("\nUnique values in each column:")
    for column in df.columns:
        print(f"{column}: {df[column].nunique()} unique values")
    
    # Display rows with null values and ask about removing them
    if df.isnull().any().any():
        print("\nRows with null values found:")
        display(df[df.isnull().any(axis=1)])
        if input("Do you want to remove all rows with null values? (yes/no): ").lower() == 'yes':
            df = df.dropna()
            print("Null values removed.")
    else:
        print("\nNo null values in DataFrame.")
    
    # Statistics and detection of outliers for each numerical column
    print("\nStatistics and Outliers for each column:")
    for column in df.select_dtypes(include=[np.number]).columns:
        print(f"\nStatistics for {column}:")
        print(df[column].describe())
        q1 = df[column].quantile(0.25)
        q3 = df[column].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
        print("Outliers:")
        if not outliers.empty:
            display(outliers)
        else:
            print("No outliers detected.")

