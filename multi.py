import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


data = pd.read_csv('Sales_Records.csv')
items = data['Item Type']
sold = data['Units Sold']

   
food_items = []
unit_sold = []


for x in items:
        
    if len(food_items) is not 5:
        food_items.append(x)
        food_items = list(set(food_items))

# print(food_items)

for y in sold:
    
    if len(unit_sold) is not 5:
        unit_sold.append(y)
        unit_sold = list(set(unit_sold))
        
# print(unit_sold)

colors = ['#008fd5', '#444444', '#fc4f30', '#e5ae37', '#6d904f']

explode = [0, 0, 0.1, 0, 0]

plt.pie(unit_sold, labels=food_items, colors=colors, explode=explode, shadow=True, autopct='%1.1f%%', startangle=90, wedgeprops={'edgecolor' : 'black'})


plt.title("Sales Records Pie Chart ")
plt.tight_layout()
plt.savefig('piechart.png')
plt.show()
