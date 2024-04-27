import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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

    # Visualization of distributions
    num_cols = df.select_dtypes(include=[np.number]).columns.size
    cat_cols = df.select_dtypes(include=['object', 'category']).columns.size
    
    total_cols = num_cols + cat_cols
    cols_per_row = 3
    rows = (total_cols + cols_per_row - 1) // cols_per_row  # Round up division
    
    plt.figure(figsize=(5 * cols_per_row, 5 * rows))
    
    for i, column in enumerate(df.columns):
        plt.subplot(rows, cols_per_row, i + 1)
        if df[column].dtype == 'object' or df[column].dtype.name == 'category':
            sns.countplot(x=df[column])
            plt.xticks(rotation=45, ha='right')
        else:
            df[column].hist()
            plt.ylabel('Frequency')
        plt.title(f'Distribution of {column}')
    
    plt.tight_layout()
    plt.show()

# Example usage:
# df = pd.read_csv('your_data.csv')
# analyze_dataframe(df)
