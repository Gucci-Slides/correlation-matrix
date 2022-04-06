#!/usr/bin/env python
# coding: utf-8

# # Imports

# In[36]:


import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# # Ticker List, Scrape Data from Yahoo Finance

# In[ ]:


# ticker list and create dataframe for 1yr performance of stock data

tickers = ['QQQ', 'TSLA', 'AAPL', 'MSFT', 'AMD', 'PYPL', 'NVDA', 'FB', 'CRWD', 'MRNA', 'AMZN'] #ticker list

df = yf.download(tickers, period="1d", start="2021-01-01", end="2022-01-01") # yahoo finance


# # Index by Closing Price, Calculate Daily Percent Change

# In[33]:


adj_close = df['Adj Close'] #index by adjusted close
returns = adj_close.pct_change() #daily change in price


# # Stock Charts

# In[54]:


# charting
adj_close.plot(figsize=(10,20), subplots=True) 
plt.show()


#  # Correlation Matrix 

# In[37]:


correlation_matrix = returns.corr()

plt.figure(figsize = (16, 6))
sns.heatmap(correlation_matrix, annot=True)
plt.show()


# # Minimum, Maximum Correlation & Std Dev Values 

# In[43]:


#miximum correlation
print(f"Maximum correlation: {correlation_matrix.min().max()}")
np.fill_diagonal(correlation_matrix.values, 0)

#maximum correlation
print(f"Maximum correlation: {correlation_matrix.max().max()}")
np.fill_diagonal(correlation_matrix.values, 1)

#standard deviation
print('\n standard deviation\n', adj_close.std())


# In[ ]:




