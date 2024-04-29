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
    #for column in df.select_dtypes(include=[np.number]).columns:
    #    print(f"\nStatistics for {column}:")
    print(df[column].describe())


    # # Function to detect outliers
    def detect_outliers(series):
        Q1 = series.quantile(0.25)
        Q3 = series.quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        return series[(series < lower_bound) | (series > upper_bound)]

    
    # Visualization of distributions
    # Ask about visualization for each column
    for column in df.columns:
        response = input(f"Plot the distribution for {column}?: ").lower()
        if response == 'yes':
            plt.figure(figsize=(6, 6))
            if df[column].dtype == 'object' or df[column].dtype.name == 'category':
                sns.countplot(x=df[column])
                plt.xticks(rotation=45, ha='right')
                plt.title(f'Count Plot for {column}')
            else:
                df[column].hist()
                plt.ylabel('Frequency')
                plt.title(f'Histogram for {column}')
            plt.show()


# Example usage:
# df = pd.read_csv('your_data.csv')
# analyze_dataframe(df)
