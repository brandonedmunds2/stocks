import numpy as np
import pandas as pd
import yfinance as yf
import os
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import interface


def load_tickers(args):
    dfs = []
    for f in os.listdir(args.ticker_directory_path):
        dfs.append(pd.read_csv(os.path.join(args.ticker_directory_path, f)))
    tickers = pd.concat(dfs).iloc[:, 0]
    tickers = tickers.dropna().values
    return tickers


def annual_perc(tickers):
    end = datetime.now()
    end1 = end - timedelta(days=3)
    start = end - timedelta(weeks=52)
    start1 = start + timedelta(days=3)
    start_data = yf.download(
        ' '.join(tickers), start=start, end=start1).iloc[0, :]['Close']
    end_data = yf.download(' '.join(tickers), start=end1,
                           end=end).iloc[-1, :]['Close']
    perc = end_data/start_data
    perc = perc.dropna()
    return perc


def main():
    args = interface.get_args()
    interface.setup_env(args)
    tickers = load_tickers(args)
    perc = annual_perc(tickers)
    perc.to_csv(os.path.join(args.output_directory_path, "perc.csv"))
    perc.sort_values(ascending=False)[:20].plot.bar()
    plt.show()


if __name__ == "__main__":
    main()
