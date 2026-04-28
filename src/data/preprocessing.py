import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Full data cleaning pipeline based on the original notebook.
    """

    df = df.copy()

    # -------------------------------------------------
    # 1) Basic info checks (optional – for debugging)
    # -------------------------------------------------
    # print(df.shape)
    # print(df.info())
    # print(df.isna().sum())

    # -------------------------------------------------
    # 2) Count missing values per row
    # -------------------------------------------------
    df['missing_count'] = df.isna().sum(axis=1)

    # -------------------------------------------------
    # 3) Remove zero Bitcoin price rows
    # -------------------------------------------------
    if 'btc_market_price' in df.columns:
        df = df[df['btc_market_price'] != 0]

    df = df.reset_index(drop=True)

    # -------------------------------------------------
    # 4) Convert Date column
    # -------------------------------------------------
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        df = df.sort_values('Date')
        df = df.drop_duplicates(subset=['Date'])
        df = df.set_index('Date')

    # -------------------------------------------------
    # 5) Interpolate selected numeric columns
    # -------------------------------------------------
    cols = [
        'btc_total_bitcoins',
        'btc_trade_volume',
        'btc_blocks_size',
        'btc_median_confirmation_time',
        'btc_difficulty',
        'btc_transaction_fees'
    ]

    existing_cols = [c for c in cols if c in df.columns]
    df[existing_cols] = df[existing_cols].interpolate(method='linear')

    # -------------------------------------------------
    # 6) Recalculate market cap and check multicollinearity
    # -------------------------------------------------
    if 'btc_market_price' in df.columns and 'btc_total_bitcoins' in df.columns:
        df['calc_market_cap'] = df['btc_market_price'] * df['btc_total_bitcoins']

        if 'btc_market_cap' in df.columns:
            diff_ratio = (
                (df['calc_market_cap'] - df['btc_market_cap']).abs()
                / df['btc_market_cap']
            )
            print("Mean % difference:", diff_ratio.mean() * 100)

            # Drop original market cap (as in notebook)
            df = df.drop('btc_market_cap', axis=1)

    # -------------------------------------------------
    # 7) Drop useless columns
    # -------------------------------------------------
    drop_cols = ['missing_count', 'btc_n_transactions_total']
    existing_drop = [c for c in drop_cols if c in df.columns]
    df = df.drop(existing_drop, axis=1)

    return df
