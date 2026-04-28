import pandas as pd
from statsmodels.tsa.stattools import adfuller, kpss

def check_stationarity(series: pd.Series, name: str):
    """Perform ADF and KPSS tests on a time series."""
    print(f"\n===== {name} =====")

    # ADF Test
    adf_result = adfuller(series, autolag='AIC')
    print("ADF Test:")
    print(f"Statistic: {adf_result[0]:.4f}, p-value: {adf_result[1]:.4f}")

    # KPSS Test
    kpss_result = kpss(series, regression='c', nlags='auto')
    print("KPSS Test:")
    print(f"Statistic: {kpss_result[0]:.4f}, p-value: {kpss_result[1]:.4f}")
    for key, value in kpss_result[3].items():
        print(f"Critical ({key}): {value}")

    return {"ADF": adf_result, "KPSS": kpss_result}
