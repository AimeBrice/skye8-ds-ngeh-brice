import pandas as pd
import pytest


@pytest.fixture
def sample_price_data() -> pd.DataFrame:
    """
    Create sample price data for testing.

    Returns:
        Example dataframe.
    """
    return pd.DataFrame(
        {
            "product": ["Laptop", "Phone", "Tablet"],
            "price": [1000, 500, None],
        }
    )
