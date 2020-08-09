# O.Kürşat Karayılan
# 150140011

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("AAPL.csv") 

def chart(default, date1, date2):
	if(default == 1):
		print("Average val: {}".format(df["Close"].mean()))
		print("Standard deviation val: {}".format(df["Close"].std()))
		rms = df["Close"]**2
		rms = rms.mean()
		rms = rms**(1/2)
		print("Root mean square val: {}".format(rms))
		rolling_mean = df.Close.rolling(window=3).mean()
		df.Close.plot(figsize=(16,8), title="Apple")
		plt.plot(rolling_mean, label='3 Day SMA', color='orange', alpha=0.5)
		plt.legend(loc='upper left')
		plt.show()
	else:
		mask = (df['Date'] > date1) & (df['Date'] <= date2)
		df2 = df.loc[mask]
		print("Average val: {}".format(df2["Close"].mean()))
		print("Standard deviation val: {}".format(df2["Close"].std()))
		rms = df2["Close"]**2
		rms = rms.mean()
		rms = rms**(1/2)
		print("Root mean square val: {}".format(rms))
		rolling_mean = df2.Close.rolling(window=3).mean()
		df2.Close.plot(figsize=(16,8), title="Apple")
		plt.plot(rolling_mean, label='3 Day SMA', color='orange', alpha=0.5)
		plt.legend(loc='upper left')
		plt.show()

print("Please enter date interval. If you enter blank input to first date, default will be all dates.\n")
first = input("Enter first date(YYYY-MM-DD): ")
if(first==""):
	chart(1, 0, 0)
else:
	second = input("Enter second date(YYYY-MM-DD): ")
	chart(0, first, second)

