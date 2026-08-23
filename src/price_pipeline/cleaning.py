import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean raw price data.

    Args:
        df: Raw input dataframe.

    Returns:
        Cleaned dataframe.
    """
    return df.dropna()
