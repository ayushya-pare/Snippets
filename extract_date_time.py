import pandas as pd

def extract_date_time(df, date_column, date_format=None, include_time=False):
    """
    This function takes a DataFrame and the name of a column containing datetime information.
    It extracts the day, month, and year from the datetime column, and optionally the hour, minute,
    and second if include_time is True. It adds these as new columns in the DataFrame.
    
    Parameters:
        df (pandas.DataFrame): The DataFrame containing the datetime information.
        date_column (str): The name of the column with datetime values.
        date_format (str, optional): The string format of the datetime column if it needs parsing.
                                     If None, it is assumed the column is already in datetime format.
        include_time (bool, optional): If True, hour, minute, and second will be extracted alongside the date.
    
    Returns:
        pandas.DataFrame: A DataFrame with the original data and new columns for the day, month, year,
                          and optionally hour, minute, and second.
    """
    # Check if datetime parsing is required
    if date_format:
        df[date_column] = pd.to_datetime(df[date_column], format=date_format)
    
    # Extract day, month, and year into separate columns
    df[date_column + '_day'] = df[date_column].dt.day
    df[date_column + '_month'] = df[date_column].dt.month
    df[date_column + '_year'] = df[date_column].dt.year

    # Extract time components if requested
    if include_time:
        df[date_column + '_hour'] = df[date_column].dt.hour
        df[date_column + '_minute'] = df[date_column].dt.minute
        df[date_column + '_second'] = df[date_column].dt.second

    return df

