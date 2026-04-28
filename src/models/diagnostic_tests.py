import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def get_vecm_roots(vecm_model_fit):
    """
    Compute eigenvalues of the VECM companion matrix
    """

    alpha = vecm_model_fit.alpha
    beta = vecm_model_fit.beta
    gamma = vecm_model_fit.gamma

    k = alpha.shape[0]

    Pi = alpha @ beta.T

    p = gamma.shape[1] // k

    gammas = [gamma[:, i*k:(i+1)*k] for i in range(p)]

    top_row = np.hstack([Pi] + gammas)

    if p > 0:
        bottom = np.hstack([
            np.eye(k*p),
            np.zeros((k*p, k))
        ])
        companion = np.vstack([top_row, bottom])
    else:
        companion = top_row

    eigenvalues = np.linalg.eigvals(companion)

    return eigenvalues


def plot_roots(roots):
    """
    Plot eigenvalues against unit circle
    """

    fig, ax = plt.subplots(figsize=(6,6))

    circle = plt.Circle((0,0),1,color='black',fill=False,linestyle='--')
    ax.add_artist(circle)

    ax.scatter(np.real(roots), np.imag(roots))

    ax.axhline(0)
    ax.axvline(0)

    ax.set_title("VECM Stability (Eigenvalues)")
    ax.set_xlabel("Real")
    ax.set_ylabel("Imaginary")

    ax.set_aspect("equal")

    plt.show()


def residual_summary(vecm_model_fit):

    resid = vecm_model_fit.resid

    df = pd.DataFrame({
        "mean": resid.mean(axis=0),
        "std": resid.std(axis=0),
        "skew": pd.DataFrame(resid).skew(),
        "kurtosis": pd.DataFrame(resid).kurt()
    })

    return df


def ecm_significance(vecm_model_fit):
    """
    Extract alpha coefficients (error correction speeds)
    """

    alpha = vecm_model_fit.alpha
    stderr = vecm_model_fit.stderr_alpha
    tvals = alpha / stderr

    df = pd.DataFrame({
        "alpha": alpha.flatten(),
        "std_err": stderr.flatten(),
        "t_stat": tvals.flatten()
    })

    return df


def diagnostic_tests(vecm_model_fit, plot=True):

    print("\n==============================")
    print("VECM DIAGNOSTIC REPORT")
    print("==============================")

    # number of lags
    k = vecm_model_fit.alpha.shape[0]
    p = vecm_model_fit.gamma.shape[1] // k

    print(f"\nLagged differences (k_ar_diff): {p}")
    print(f"Number of variables: {k}")

    # --------------------------
    # 1 Autocorrelation
    # --------------------------

    try:
        autocorr = vecm_model_fit.test_whiteness(nlags=10)

        print("\n1. Portmanteau Test (Residual Autocorrelation)")
        print(autocorr.summary())
        print("\nNote: For crypto data this test is often rejected.")

    except Exception:
        autocorr = None
        print("\n1. Portmanteau test not available.")

    # --------------------------
    # 2 Stability
    # --------------------------

    roots = get_vecm_roots(vecm_model_fit)

    is_stable = np.all(np.abs(roots) < 1)

    print("\n2. Stability Test")
    print("------------------")
    print("Eigenvalues:")
    print(roots)

    print("\nAll roots inside unit circle:", is_stable)

    if plot:
        plot_roots(roots)

    # --------------------------
    # 3 Normality
    # --------------------------

    try:

        normality = vecm_model_fit.test_normality()

        print("\n3. Normality Test (Jarque-Bera)")
        print(normality.summary())
        print("\nNote: Financial time series almost always reject normality.")

    except Exception:
        normality = None
        print("\n3. Normality test not available.")

    # --------------------------
    # 4 ECM coefficients
    # --------------------------

    print("\n4. Error-Correction Speeds (alpha)")
    print("----------------------------------")

    alpha_table = ecm_significance(vecm_model_fit)

    print(alpha_table)

    # --------------------------
    # 5 Residual statistics
    # --------------------------

    print("\n5. Residual Distribution Summary")
    print("--------------------------------")

    resid_stats = residual_summary(vecm_model_fit)

    print(resid_stats)

    return {
        "autocorrelation": autocorr,
        "normality": normality,
        "roots": roots,
        "is_stable": is_stable,
        "alpha_table": alpha_table,
        "residual_summary": resid_stats
    }
