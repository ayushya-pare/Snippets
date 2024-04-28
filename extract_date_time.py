import pandas as pd

def extract_date_parts(df, date_column, date_format=None):
    """
    This function takes a DataFrame and the name of a column containing date information.
    It extracts the day, month, and year from the date column and adds these as new columns in the DataFrame.
    
    Parameters:
        df (pandas.DataFrame): The DataFrame containing the date information.
        date_column (str): The name of the column with date values.
        date_format (str, optional): The string format of the date column if it needs parsing.
                                     If None, it is assumed the column is already in datetime format.
    
    Returns:
        pandas.DataFrame: A DataFrame with the original data and new columns for the day, month, and year.
    """
    # Check if date parsing is required
    if date_format:
        df[date_column] = pd.to_datetime(df[date_column], format=date_format)
    
    # Extract day, month, and year into separate columns
    df[date_column + '_day'] = df[date_column].dt.day
    df[date_column + '_month'] = df[date_column].dt.month
    df[date_column + '_year'] = df[date_column].dt.year

    return df

