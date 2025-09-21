import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy import random
import seaborn as sns

np.random.seed(42)
trading_date = pd.date_range(start='2024-01-01', end='2024-12-31', freq='B')
median_stock = [23, 41, 56, 38, 47]
company_names = ['company_1', 'company_2', 'company_3', 'company_4', 'company_5']
stock_market_data = pd.DataFrame()

for i, company in enumerate(company_names):
    mean_price = median_stock[i]
    stock_price = random.normal(mean_price, 2, size=len(trading_date))
    stock_market_data[company] = stock_price

stock_market_data['trading_date'] = trading_date
stock_market_data = stock_market_data.set_index('trading_date')
print(stock_market_data)

daily_returns = stock_market_data.apply(lambda x: (x - x.shift(1)) / x.shift(1)).dropna()
print(daily_returns)
cumulative_returns = (1+daily_returns).cumprod() - 1
print(cumulative_returns)
monthly_returns = stock_market_data.resample('ME').last().pct_change()
print(monthly_returns)

monthly_returns_corr = monthly_returns.corr()
corr_matrix = daily_returns.corr()
cum_corr_matrix = cumulative_returns.corr()

plt.subplot(2, 2, 1)
plt.plot(stock_market_data.index, stock_market_data['company_1'], label='company_1', color='blue')
plt.plot(stock_market_data.index, stock_market_data['company_2'], label='company_2', color='red')
plt.plot(stock_market_data.index, stock_market_data['company_3'], label='company_3', color='black')
plt.plot(stock_market_data.index, stock_market_data['company_4'], label='company_4', color='green')
plt.plot(stock_market_data.index, stock_market_data['company_5'], label='company_5', color='yellow')
plt.legend(loc='best')
plt.grid()

plt.subplot(2, 2, 2)
sns.heatmap(cum_corr_matrix, annot=True, cmap='coolwarm', center=0, linewidths=.5)

plt.subplot(2, 2, 3)
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, linewidths=.5)

plt.subplot(2, 2, 4)
sns.heatmap(monthly_returns_corr, annot=True, cmap='coolwarm', center=0, linewidths=.5)

plt.show()