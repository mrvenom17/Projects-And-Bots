# utils.py

def clean_data(df):
    """Clean and preprocess scraped data."""
    df.dropna(inplace=True)
    df['price'] = df['price'].astype(float)
    return df