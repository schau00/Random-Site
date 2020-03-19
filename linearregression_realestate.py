# -*- coding: utf-8 -*-
"""LinearRegression_RealEstate.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WDGy4O87Maoe_AGpdr-RH_XtxIJsBB-7
"""

import numpy as np
import pandas as pd
import scipy
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn

dataset = pd.read_csv('real_estate_price_size.csv')

dataset.describe()

dataset.shape

"""# A Scatter Plot Representing the Variations of **SIZE** of Real Estate wrt **PRICE** using ***Matplotlib***"""

x=dataset['price']
y=dataset['size']
plt.scatter(x,y,label='size')
plt.title('REAL ESTATE\nPRICE VS SIZE')
plt.xlabel('Price')
plt.ylabel('Size')
plt.legend()
plt.show()

"""# A Scatter Plot Representing the Variations of **PRICE** of Real Estate wrt **SIZE** using ***Matplotlib***

x axis : SIZE
y axis : PRICE
"""

x= dataset['size']
y=dataset['price']
plt.scatter(x,y,label='price',color='green')
plt.xlabel('SIZE')
plt.ylabel('PRICE')
plt.title('REAL ESTATE\nSIZE VS PRICE')
plt.legend()
plt.show()

"""This is a single variable linear regression of the form 
y = a + b*x
# To determine the value of a,b the **OLS**(Ordinary Least Square) method is implemented using **Statsmodel**

x axis : SIZE
y axis : PRICE
"""

y = dataset['price']
x = dataset['size']
x = sm.add_constant(x)
# a constant is added to predictor x

# perform OLS
z = sm.OLS(y,x).fit()
z.summary()

print(x)
x1 = dataset['size'] 
#print(x1)
#converted a 2-d x array to 1-d x1 array
#plt.scatter(x1,y)

plt.scatter(x1,y)
yhat = 101900 + 223.1787*x1
regr = plt.plot(x1,yhat,color='red',label='Regression Line SIZE vs PRICE')
plt.legend()
plt.ylabel('Price')
plt.xlabel('Size')
plt.title('REAL ESTATE\nRegression Line')
plt.show()

"""x axis : PRICE
y axis : SIZE
"""

x = dataset['price']
y = dataset['size']
x = sm.add_constant(x)

z = sm.OLS(y,x).fit()
z.summary()

x1 = dataset['price']
# print(x1)

plt.scatter(x1,y,color='green')
yhat = (0.0033*x1) -122.3349 
plt.plot(x1,yhat,color='red',label='Regression Line PRICE vs SIZE')
plt.xlabel('Price')
plt.ylabel('Size')
plt.title('REAL ESTATE\nREGRESSION LINE')
plt.legend()
plt.show()