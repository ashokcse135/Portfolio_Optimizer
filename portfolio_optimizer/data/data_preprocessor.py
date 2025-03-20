import pandas as pd

def check_missing_values(df):
    return df.isnull().any().any()


def impute_missing_values(df):
    pass

def extract_close_price(df) -> pd.DataFrame:
    '''
    Returns a dataframe with only Close price
    '''
    # Keep only Close column
    df = df.loc[:, (slice(None) ,"Close")]
    # Remove .NS from column names
    df.columns = [ticker.split(".")[0] for ticker in df.columns.droplevel(1)]

    return df
    
