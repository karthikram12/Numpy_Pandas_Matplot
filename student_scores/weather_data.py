import pandas as pd
import matplotlib.pyplot as plt
from numpy import random

current_date = pd.date_range('1/1/2024', '12/31/2024', freq='D')
daily_temp = random.uniform(-10, 10, size=len(current_date))
humidity = random.randint(10, 50, size=len(current_date))
windspeed = random.randint(10, 30, size=len(current_date))

weather_data = pd.DataFrame({'current_date': current_date, 'daily_temp': daily_temp, 'humidity': humidity, 'windspeed': windspeed})
weather_data = weather_data.set_index('current_date')
print(weather_data)

monthly_mean = weather_data.resample('M').mean()
print(monthly_mean)

plt.subplot(2, 2, 1)
plt.plot(weather_data.index, weather_data['daily_temp'], color='red', label='Daily Temp')
plt.plot(weather_data.index, weather_data['humidity'], color='blue', label='Humidity')
plt.plot(weather_data.index, weather_data['windspeed'], color='green', label='Wind Speed')
plt.xlabel('Date')
plt.ylabel('Measurement')
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(monthly_mean.index, monthly_mean['daily_temp'], color='red')
plt.xlabel('Date')
plt.ylabel('Measurement')

plt.subplot(2, 2, 3)
plt.scatter(weather_data['daily_temp'], weather_data['humidity'], color='red')
plt.xlabel('Daily Temp')
plt.ylabel('Humidity')

plt.subplot(2, 2, 4)
plt.plot(monthly_mean.index, monthly_mean['humidity'], color='red', label='Humidity')
plt.plot(monthly_mean.index, monthly_mean['daily_temp'], color='blue', label='Daily Temp')
plt.plot(monthly_mean.index, monthly_mean['windspeed'], color='green', label='Windspeed')
plt.xlabel('Date')
plt.ylabel('Measurement')
plt.legend(loc='center')

plt.show()