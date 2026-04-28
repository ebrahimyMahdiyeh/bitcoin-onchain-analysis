import numpy as np
import matplotlib.pyplot as plt

def plot_log_series(df, columns):
    fig, axes = plt.subplots(len(columns), 1, figsize=(14, 18), sharex=True)

    for i, col in enumerate(columns):
        axes[i].plot(df.index, np.log(df[col]), linewidth=1)
        axes[i].set_title(f"log_{col}")
        axes[i].grid(True)

    plt.tight_layout()
    plt.show()
