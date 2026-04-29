Bitcoin On-Chain Analysis – Project Description (Clean Text Version)
Title: Bitcoin On-Chain Analysis

Summary:
This project provides an empirical investigation of the relationship between Bitcoin market prices and on-chain or network-based metrics—particularly hash rate—using cointegration analysis and a Vector Error Correction Model (VECM). The goal is to rigorously test whether stable long-term relationships exist between these variables and to identify which variables adjust to restore long‑run equilibrium.

Project Objectives:
Evaluate whether a long‑run cointegration relationship exists between Bitcoin price and selected on‑chain metrics.
Identify the variables responsible for correcting deviations from long‑term equilibrium (error‑correction behavior).
Provide a clear, replicable, and transparent econometric pipeline for analyzing Bitcoin with time‑series methods.
Methodology:

Daily data from Yahoo Finance (prices) and CoinMetrics (on‑chain indicators).
Preprocessing steps include logarithmic transformation, differencing, and series alignment.
Unit‑root testing and determination of cointegration rank.
Estimation and interpretation of the VECM system.
Diagnostic checks:• Stability (eigenvalues inside the unit circle)• Residual autocorrelation (Portmanteau test; interpreted informally due to financial‑data properties)• Residual normality (Jarque–Bera; non‑normality is expected for market data)
Project Structure:

data/ – raw and processed datasets
notebooks/ – Jupyter notebooks for preprocessing, model estimation, and diagnostics
src/ – modular Python code (data loading, models, diagnostics, utilities)
results/ – stored model outputs, figures, and plots
requirements.txt
README.md

Installation and Usage:
Clone the repository:git clone https://github.com/yourusername/bitcoin-onchain-analysis.git
Change directory:cd bitcoin-onchain-analysis
Create and activate a Python virtual environment.
Install dependencies using:pip install -r requirements.txt
Launch Jupyter Notebook:jupyter notebook
The main analysis notebooks are located in the notebooks/ directory (such as 03_vecm_model.ipynb and 04_diagnostics.ipynb).

Notes and Limitations:
Crypto markets exhibit high volatility, heavy‑tailed distributions, and regime shifts.
Therefore, diagnostic tests (Portmanteau, normality) should be interpreted as informational rather than strict decision criteria.
The analysis focuses primarily on system stability, coefficient significance, and the existence of long‑run relationships between price and network metrics.
