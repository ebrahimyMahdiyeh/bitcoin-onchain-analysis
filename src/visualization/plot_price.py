import matplotlib.pyplot as plt

def plot_price(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['btc_market_price'])
    plt.title("Bitcoin Price 2010–2018")
    plt.grid(True)
    plt.show()
