import pandas as pd

def clean_data(df):
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Handle missing values
    df.fillna(method='ffill', inplace=True)
    
    return df


def convert_date(df, column):
    df[column] = pd.to_datetime(df[column], errors='coerce')
    return df