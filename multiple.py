import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


data = pd.read_csv('Sales_Records.csv')
items = data['Item Type']
sold = data['Units Sold']
price = data['Unit Price']

   
food_items = []
unit_sold = []
unit_price = []

for x in items:
        
    if len(food_items) is not 10:
        food_items.append(x)
        food_items = list(set(food_items))

# print(food_items)

for y in sold:
    
    if len(unit_sold) is not 10:
        unit_sold.append(y)
        unit_sold = list(set(unit_sold))
        
# print(unit_sold)

for z in price:
    
    if len(unit_price) is not 10:
        unit_price.append(z)
        unit_price = list(set(unit_price))
        
# print(unit_price)


x_indexes = np.arange(len(food_items))
width = 0.4

plt.barh(x_indexes + width , unit_price, width, color='#e5ae37', label='Unit Price')
plt.barh(x_indexes, unit_sold, width, color='#008fd5', label='Units Sold')
#barh plots barchart horizontally
    
    
plt.yticks(ticks=x_indexes, labels=food_items)

plt.xlabel('Units Sold Out on what Price')
plt.ylabel('Number of Food Items')
plt.title('Sales Records')
plt.legend()

plt.tight_layout()
plt.savefig('barchart.png')

plt.show()
