import pandas as pd
from pathlib import Path

def load_data(filename: str):
    """
    Loads raw CSV data from the data/raw directory.
    """
    filepath = Path("data/raw") / filename
    df = pd.read_csv(filepath)
    return df