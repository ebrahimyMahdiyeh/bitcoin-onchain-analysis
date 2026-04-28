from statsmodels.tsa.api import VAR

def select_var_lag(data, maxlags=15):
    """Select optimal lag using standard criteria (AIC, BIC, HQIC, FPE)."""
    model = VAR(data)
    lag_results = model.select_order(maxlags)
    print(lag_results.summary())
    return lag_results
