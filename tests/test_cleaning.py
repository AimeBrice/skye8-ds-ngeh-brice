from price_pipeline.cleaning import clean_data


def test_clean_data_removes_missing_values(sample_price_data):
    """
    Test that cleaning removes missing values.
    """

    cleaned = clean_data(sample_price_data)

    assert cleaned.isnull().sum().sum() == 0
