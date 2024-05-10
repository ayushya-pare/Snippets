import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_dataframe(df):
    
    # Check if the first column is the index or unnamed, then remove it if necessary
    if df.columns[0] == df.index.name or df.columns[0].startswith('Unnamed'):
        print("\nThe first column is either the index or unnamed, removing it.")
        df.drop(df.columns[0], axis=1, inplace=True)
        if df.columns.size > 0:
            print("\nThe new first column is:", df.columns[0])
        else:
            print("\nNo columns left after removal.")
    else:
        print("\nThe first column is not the index, it is:", df.columns[0])

    # Clean column names by removing spaces
    df.columns = df.columns.str.replace(' ', '_')
    
    # Check for duplicates and remove them
    num_duplicates = df.duplicated().sum()
    if num_duplicates > 0:
        print(f"\n{num_duplicates} duplicate rows found.")
        response = input("Do you want to remove duplicates? (yes/no): ").lower()
        if response == 'yes':
            df = df.drop_duplicates(inplace = Trure)
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

    # Show unique values in each column
    print("\nUnique values in each column:")
    for column in df.columns:
        print(f"{column}: {df[column].nunique()} unique values")

    # Display rows with null values and ask about removing them
    if df.isnull().any().any():
        print("\nRows with null values found:")
        display(df[df.isnull().any(axis=1)])
        if input("Do you want to remove all rows with null values? (yes/no): ").lower() == 'yes':
            df = df.dropna(inplace = True)
            print("Null values removed.")
    else:
        print("\nNo null values in DataFrame.")

    # Statistics and detection of outliers for each numerical column
    print("\nStatistics for the dataset:")
    df.describe()

    # Correlation heatmap
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    corr = df[numeric_cols].corr()

    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.show()

    # Normalize numerical columns and save in a temporary variable
    normalized_df = df.select_dtypes(include=[np.number]).apply(lambda x: (x - x.mean()) / x.std(), axis=0)

    # Visualization of count plots for categorical columns
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns
    if len(categorical_cols) > 0:
        #fig, axes = plt.subplots(nrows=(len(categorical_cols) + 1) // 2, ncols=1, figsize=(12, 6))
        #fig.suptitle('Bar Plots for Categorical Columns')
        #axes = axes.flatten()  # Flatten axes array for easy iteration
        for idx, column in enumerate(categorical_cols):
            sns.countplot(x=df[column])
            #axes[idx].set_title(f'Count Plot for {column}')
            #axes[idx].tick_params(axis='x', rotation=45)
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.show()

    # Visualization of histograms for numerical columns
    numerical_cols = df.select_dtypes(include=[np.number]).columns
    if len(numerical_cols) > 0:
        df.hist(column=numerical_cols, figsize=(12, 6), bins=15)
        plt.suptitle('Histograms for Numerical Columns')
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.show()

    # Boxplots of all normalized numerical columns
    if len(numerical_cols) > 0:
        plt.figure(figsize=(12, 6))
        ax = sns.boxplot(data = normalized_df)
        plt.xticks(rotation=45)
        plt.title('Boxplots of Normalized Numerical Columns')
        plt.show()


# Example usage:
# df = pd.read_csv('your_data.csv')
