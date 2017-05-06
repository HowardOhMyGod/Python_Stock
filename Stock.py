
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import re

stock = pd.read_csv('C:\\Users\\Howard\\Desktop\\jupyter\\stock.csv',low_memory=False)
stock = stock.iloc[1:]
stock = stock.rename(columns = {'Unnamed: 0':'Date'})
stock = stock.set_index('Date')

for column in stock:
    stock[column] = stock[column].astype(str)
    stock[column] = stock[column].map(lambda col: re.sub(r',+', '', col))
    
stock = stock.replace('nan', np.nan)
stock = stock.apply(pd.to_numeric)


# In[2]:

stock.head()


# In[3]:

stock_return = stock.apply(lambda col: ((col - col.shift(1, axis = 0))/ col.shift(1, axis = 0)), axis = 0)
stock_return = stock_return.iloc[1:]

stock_return_mean = stock_return.apply(np.mean)
stock_return_mean = stock_return_mean*252
stock_return_mean = stock_return_mean[(stock_return_mean > 0) & (stock_return_mean < 0.2)]


stock_return_var = stock_return.apply(np.var)
stock_return_var = stock_return_var * 252
stock_return_var = stock_return_var[stock_return_var < 1]
# stock_return_var

total = pd.concat([stock_return_mean, stock_return_var], axis=1)
total.columns = ['Mean', 'Var']

import matplotlib
get_ipython().magic('matplotlib inline')
total.plot(x = 'Var', y = 'Mean', kind='scatter')



# In[ ]:



