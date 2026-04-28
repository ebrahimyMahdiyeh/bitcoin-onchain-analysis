import matplotlib.pyplot as plt

def plot_with_moving_averages(
    df, ax, column,
    start=None, end=None,
    short_window=30, long_window=90,
    log_scale=False
):
    data = df.loc[start:end, column]

    short_ma = data.rolling(short_window).mean()
    long_ma  = data.rolling(long_window).mean()

    ax.plot(data.index, data, label=column, alpha=0.7)
    ax.plot(short_ma.index, short_ma, label=f"SMA {short_window}", linewidth=2)
    ax.plot(long_ma.index, long_ma, label=f"SMA {long_window}", linewidth=2)

    if log_scale:
        ax.set_yscale("log")

    ax.legend()


def plot_ma_for_columns(df, columns, start, end, short=20, long=120):
    fig, axes = plt.subplots(len(columns), 1, figsize=(14, 18), sharex=True)

    for i, col in enumerate(columns):
        plot_with_moving_averages(
            df=df, ax=axes[i], column=col,
            start=start, end=end,
            short_window=short, long_window=long,
            log_scale=True
        )
        axes[i].set_title(f"log_{col}")
        axes[i].grid(True)

    plt.tight_layout()
    plt.show()
