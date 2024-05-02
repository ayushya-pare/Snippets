import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_dataframe(df):
    # Clean column names by removing spaces
    df.columns = df.columns.str.replace(' ', '_')
    
    # Check for duplicates and remove them
    num_duplicates = df.duplicated().sum()
    if num_duplicates > 0:
        print(f"\n{num_duplicates} duplicate rows found.")
        response = input("Do you want to remove duplicates? (yes/no): ").lower()
        if response == 'yes':
            df = df.drop_duplicates()
            print("Duplicates removed.")
        else:
            print("Duplicates not removed.")
    else:
        print("\nNo duplicates found.")

    # Display basic information about the DataFrame
    print("\nDataFrame Info:")
    df.info()

    # Show columns and their data types
    print("\nColumns and their Data Types:")
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
    print("\nStatistics and Outliers for each numerical column:")
    for column in df.select_dtypes(include=[np.number]).columns:
        print(f"\nStatistics for {column}:")
        print(df[column].describe())

    # Correlation heatmap
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    corr = df[numeric_cols].corr()

    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm',    vmax=1,
        fmt=".2f",
        annot=True,
        center=0,
        square=True,
        linewidths=0.5,
        cbar_kws={"shrink": 0.5})
    plt.title('Correlation Heatmap')
    plt.show()

    # Visualization of distributions for individual columns
    for column in df.columns:
        response = input(f"Plot the distribution for {column}?: ").lower()
        if response == 'yes':
            if df[column].dtype == 'object' or df[column].dtype.name == 'category':
                plt.figure(figsize=(8, 6))
                sns.countplot(x=df[column])
                plt.xticks(rotation=45, ha='right')
                plt.title(f'Count Plot for {column}')
                plt.show()
            else:
                # Creating histograms and boxplots for numeric columns
                fig, axes = plt.subplots(1, 2, figsize=(12, 6))
                
                # Histogram plot
                df[column].hist(ax=axes[0])
                axes[0].set_ylabel('Frequency')
                axes[0].set_title(f'Histogram for {column}')

                # Boxplot plot
                df[[column]].boxplot(ax=axes[1], grid=False)
                axes[1].set_title(f'Boxplot for {column}')

                plt.tight_layout()
                plt.show()
        elif response == 'exit':
            break

# Example usage:
# df = pd.read_csv('your_data.csv')
# analyze_dataframe(df)
