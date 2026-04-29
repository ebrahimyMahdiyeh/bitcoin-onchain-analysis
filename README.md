# Bitcoin On-Chain Analysis – Project Description

## Summary
This project provides an empirical investigation of the relationship between **Bitcoin market prices** and **on‑chain/network metrics**—particularly **hash rate**—using **cointegration analysis** and a **Vector Error Correction Model (VECM)**. The goal is to rigorously test whether **stable long‑term relationships** exist between these variables and to identify which variables adjust to restore **long‑run equilibrium**.

## Project Objectives
- Evaluate whether a **long‑run cointegration relationship** exists between Bitcoin price and selected on‑chain metrics.
- Identify the variables responsible for correcting deviations from **long‑term equilibrium (error‑correction behavior)**.
- Provide a **clear, replicable, and transparent econometric pipeline** for analyzing Bitcoin with time‑series methods.

## Methodology
- Data from **CoinMetrics**
- Preprocessing steps include **logarithmic transformation**, **differencing**, and **series alignment**
- **Unit‑root testing** and determination of **cointegration rank**
- Estimation and interpretation of the **VECM system**

Diagnostic checks:
- **Stability** (eigenvalues inside the unit circle)
- **Residual autocorrelation** (Portmanteau test; interpreted informally due to financial‑data properties)
- **Residual normality** (Jarque–Bera; non‑normality is expected for market data)

## Notes and Limitations
Crypto markets exhibit **high volatility**, **heavy‑tailed distributions**, and **regime shifts**.

Therefore, diagnostic tests (**Portmanteau**, **normality**) should be interpreted as **informational rather than strict decision criteria**.

The analysis focuses primarily on:
- **System stability**
- **Coefficient significance**
- **Long‑run relationships between price and network metrics**

## Project Structure
