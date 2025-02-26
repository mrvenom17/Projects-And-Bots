# utils.py

def clean_data(df):
    """Clean and preprocess scraped data."""
    df.dropna(inplace=True)
    df['price'] = df['price'].str.replace('$', '').astype(float)
    return df