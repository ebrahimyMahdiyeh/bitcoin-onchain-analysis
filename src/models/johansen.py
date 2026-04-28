from statsmodels.tsa.vector_ar.vecm import coint_johansen

def run_johansen_test(data, det_order=0, k_ar_diff=3):
    """Run Johansen cointegration test and print formatted results."""
    jres = coint_johansen(data, det_order=det_order, k_ar_diff=k_ar_diff)

    print("--- Johansen Cointegration Test Results ---")
    print(f"{'Rank':<10} {'Trace Stat':<15} {'Crit 95% (Trace)':<20} "
          f"{'Max-Eigen Stat':<15} {'Crit 95% (Max)':<20}")

    for i in range(len(jres.lr1)):
        print(f"r <= {i:<6} {jres.lr1[i]:<15.4f} {jres.cvt[i, 1]:<20.4f} "
              f"{jres.lr2[i]:<15.4f} {jres.cvm[i, 1]:<20.4f}")

    return jres
