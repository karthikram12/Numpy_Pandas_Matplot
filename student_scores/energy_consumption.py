import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy import random
import seaborn as sns

random.seed(42)
hourly_range = pd.date_range(start='2024-01-01', end='2024-01-31', freq='h')
hours = hourly_range.hour
work_hours_mask = (hours >=9) & (hours <=18)
work_values = random.normal(100, 10, size=len(hourly_range))
off_values = random.normal(20, 3, size=len(hourly_range))
energy_consumption = np.where(work_hours_mask, work_values, off_values)
temperature = random.normal(30, 5, size=len(hourly_range))

energy_data = pd.DataFrame({'hourly_range': hourly_range,'energy_consumption': energy_consumption,
                            'temperature':temperature})
energy_data = energy_data.set_index('hourly_range')

day_of_week = hourly_range.dayofweek
is_weekend = (day_of_week >= 5)
energy_data['day_type'] = np.where(is_weekend, 'Weekend', 'Weekday')

daily_average_consumption = energy_data.resample('D').mean(numeric_only=True)
day_of_week1 = daily_average_consumption.index.dayofweek
is_weekend1 = (day_of_week1 >= 5)
daily_average_consumption['day_type'] = np.where(is_weekend1, 'Weekend', 'Weekday')

energy_data['daily_rolling'] = energy_data['energy_consumption'].rolling(24).mean(numeric_only=True)

weekly_energy_series = energy_data['energy_consumption'].resample('D').mean(numeric_only=True)
weekly_energy_data = pd.DataFrame({'daily_mean': weekly_energy_series,})
weekly_energy_data['rolling_average_7d'] = weekly_energy_data['daily_mean'].rolling(7).mean()

plt.subplot(2, 2, 1)

plt.plot(energy_data.index, energy_data['energy_consumption'], label='Hourly Energy Consumption', color='blue')
plt.plot(daily_average_consumption.index, daily_average_consumption['energy_consumption'], label='Daily Average Energy Consumption', color='red')
plt.legend()

energy_data['date'] = energy_data.index.date
energy_data['hour'] = energy_data.index.hour

heatmap_data = energy_data.pivot_table(index='date', columns='hour', values='energy_consumption', aggfunc='mean')
plt.subplot(2, 2, 2)
sns.heatmap(heatmap_data, cmap='RdYlGn', linewidths=.1, linecolor='gray')

plt.subplot(2, 2, 3)
energy_correlation = energy_data['energy_consumption'].corr(energy_data['temperature'])
print(energy_correlation)
plt.scatter(energy_data['temperature'], energy_data['energy_consumption'], alpha=0.5)

plt.show()

