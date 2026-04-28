import os
import joblib
from statsmodels.tsa.vector_ar.vecm import VECM

def fit_vecm(data, k_ar_diff=3, coint_rank=1, deterministic='ci', save_model=True):
    """
    Estimate a VECM model and (optionally) save fitted results.
    Returns the fitted VECMResults object.
    """

    # 1. Fit the VECM
    vecm_model = VECM(data,
                      k_ar_diff=k_ar_diff,
                      coint_rank=coint_rank,
                      deterministic=deterministic)
    
    vecm_res = vecm_model.fit()
    print(vecm_res.summary())

    # 2. Auto-save model
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
    model_dir = os.path.join(project_root, 'results')
    os.makedirs(model_dir, exist_ok=True)
    save_path = os.path.join(model_dir, 'vecm_model.pkl')
    joblib.dump(vecm_res, save_path)

       
    return vecm_res
