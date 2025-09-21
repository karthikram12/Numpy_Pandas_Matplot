import pandas as pd
import matplotlib.pyplot as plt
from numpy import random

sales_date = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
daily_sales = random.randint(100, 1000, size=len(sales_date))
categories = random.choice(['Air Conditioner', 'Television', 'Washing Machine', 'Refrigerators'], size=len(sales_date))

sales_info = pd.DataFrame({'sales_date': sales_date, 'daily_sales': daily_sales, 'categories': categories})
sales_info = sales_info.set_index('sales_date')

sales_per_product = sales_info.groupby(['categories']).sum()
monthly_sales_total = sales_info['daily_sales'].resample('M').sum()

plt.subplot(2, 2, 1)
plt.plot(sales_info.index, sales_info['daily_sales'], color='red')
plt.xlabel('Date')
plt.ylabel('Total Sales')

plt.subplot(2, 2, 2)
plt.bar(sales_per_product.index, sales_per_product['daily_sales'], color=['blue', 'red'])
plt.xlabel('Product')
plt.ylabel('Total Sales')

plt.subplot(2, 2, 3)
plt.bar(monthly_sales_total.index, monthly_sales_total.values, color='red', width=-10, align='edge')
plt.xlabel('Date')
plt.ylabel('Total Sales')

plt.subplot(2, 2, 4)
plt.pie(sales_per_product['daily_sales'], labels=sales_per_product.index, startangle=90)

plt.grid()
plt.show()


