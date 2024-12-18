import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np

tickers = [
  "BRLUSD=X",
  "EURUSD=X",
  "JPYUSD=X",
  "GBPUSD=X",
  "AUDUSD=X",
  "CADUSD=X",
  "CHFUSD=X",
  "CNYUSD=X",
  "HKDUSD=X",
  "NZDUSD=X",
]

plt.figure(figsize=(20, 6))

today = datetime.today()
end_date = today
start_date = (today - timedelta(days=10*365))
for ticker in tickers:
    data = yf.download(ticker, start=start_date, end=end_date)
    normalized_data = data['Close'] / data['Close'].iloc[0]  
    plt.plot(normalized_data, label=f"{ticker} (Normalized)", linewidth=2)

plt.title("Normalized Proportional Changes in Major Currency Exchange Rates Against USD (10-Year Trend)")
plt.xlabel("Date")
plt.ylabel("Proportional Value (Base = 1)")
plt.grid(True)
plt.legend()
plt.ylim(bottom=0, top=1.2)
y_min, y_max = plt.ylim()  
plt.yticks(np.arange(y_min, y_max, 0.1))
plt.savefig('currencies-vs-usd.png', dpi=300)
plt.show()
