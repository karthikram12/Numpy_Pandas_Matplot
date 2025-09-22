import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

covid_data_csv = pd.read_csv('full_grouped.csv')
covid_data = pd.DataFrame(covid_data_csv)
covid_data['Date'] = pd.to_datetime(covid_data['Date'])

covid_data = covid_data.rename(columns={'Date':'date', 'Country/Region':'country', 'Confirmed':'confirmed',
                                        'Deaths':'deaths','Recovered':'recovered','Active':'active',
                                        'New cases':'new_cases','New deaths':'new_deaths',
                                        'New recovered':'new_recovered', 'WHO Region':'who_region'})

countries = list(np.unique(covid_data['country']))

unique_dates = np.sort(covid_data['date'].unique())
daily_percent_change = pd.DataFrame(index=unique_dates, columns=countries)

for country in countries:
   country_filtered = covid_data[covid_data['country'] == country].set_index('date')
   pct_change = country_filtered['confirmed'].pct_change()
   daily_percent_change[country] = pct_change

daily_percent_change = daily_percent_change.replace([np.inf, -np.inf], np.nan)
daily_percent_change = daily_percent_change.fillna(0)

doubling_rate = np.log(2)/np.log(1+daily_percent_change)
doubling_rate = doubling_rate.replace([np.inf, -np.inf], np.nan)
doubling_rate = doubling_rate.fillna(0)

doubling_rate_average = doubling_rate.mean()
high_growth_rate = doubling_rate_average.sort_values().head(5)

daily_confirmed_cases = covid_data.pivot(index='date', columns='country', values='confirmed')

plt.subplot(2,1,1)
countries_with_max_cases= covid_data.groupby('country')['confirmed'].max().sort_values(ascending=False).head(5)
plt.bar(countries_with_max_cases.index, countries_with_max_cases.values, color='blue')
plt.yscale('log')
plt.xlabel('Country')
plt.ylabel('Total Number of Confirmed Cases')

plt.subplot(2,1,2)
for country in countries_with_max_cases.index:
    plt.plot(daily_confirmed_cases.index, daily_confirmed_cases[country], label=country)
    plt.yscale('log')
    plt.xlabel('Date')
    plt.ylabel('Total Number of Confirmed Cases')

plt.legend()
plt.show()



