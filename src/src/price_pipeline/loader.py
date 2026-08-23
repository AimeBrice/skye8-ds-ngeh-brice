from pathlib import Path

import pandas as pd


def load_csv(file_path: str) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.

    Args:
        file_path: Path to the CSV file.

    Returns:
        Loaded dataset.
    """
    return pd.read_csv(Path(file_path))
