# -*- coding: utf-8 -*-
'''
pandas

stochastics and monte carlo

statistical application
'''

'''
###############################################################################
       pandas
###############################################################################
       
- an open source library providing high-performance, easy-to-use data structures 
  and data analysis tools for the Python
  
- in pandas, indexed and labeled data is managed by DataFrame class. It is similar
  to SQL database table or spreadsheet. 

'''

import pandas as pd

# create DataFrame object
df = pd.DataFrame([10, 20, 30, 40], \
                   columns = ['Numbers'], \
                   index = ['a', 'b', 'c', 'd'])
# data, title of columns, index
 
'''show index'''                  
print(df.index) # show index
'''show column names'''
print(df.columns) # show column names
'''select via index'''
print(df.ix['c']) # select via index
'''multi-select via index'''
print(df.ix[['a', 'd']]) # multi-select via index
'''another way to multi-select via index'''
print(df.ix[df.index[1:3]])
'''sum per volumn'''
print(df.sum()) # sum per volumn
'''calculation'''
ts = df ** 2
print(ts) # calculation
#%%


'''enlarg dataframe'''

import pandas as pd

# create DataFrame object
df = pd.DataFrame([10, 20, 30, 40], \
                   columns = ['Numbers'], \
                   index = ['a', 'b', 'c', 'd'])
                   
# add new column
df['floats'] = (1.5, 2.6, 3.6, 4.2)

# add new column via index
df['names'] = pd.DataFrame(['dan', 'cox', 'add', 'djw'], \
                           index = ['d', 'a', 'b', 'c'])
                           
# add new column by join function
df = df.join(pd.DataFrame([2, 4, 6, 3], index = ['a', 'd', 'c','b'], \
                          columns = ['abc',] ), how = 'outer')
# use how = 'outer' to show all potential data

# add new object to df (new row)
df = df.append(pd.DataFrame({'Numbers':66, 'floats': 4.6, 'names':'how'}, \
               index = ['y',]))
df = df.append(pd.DataFrame({'Numbers':46, 'floats': 4.2, 'names':'hos'}, \
               index = ['e',]))
df = df.append(pd.DataFrame({'Numbers':62, 'floats': 1.6, 'names':'hoc'}, \
               index = ['f',]))
df = df.append(pd.DataFrame({'Numbers':86, 'floats': 3.6, 'names':'hog'}, \
               index = ['g',]))
#%%
               
'''more information about pandas

http://pandas.pydata.org/pandas-docs/stable/


'''


'''
###############################################################################
    statistical application
###############################################################################
'''

# histogram plot

df['abc'].hist(bins = 100, figsize = (8, 6))
#%%

# QQ-plot

# quantile-quantile plot

# to verify if this distribution is normal or not

import statsmodels.api as sm
import matplotlib.pyplot as plt
sm.qqplot(df['abc'].dropna(), line = 's')
plt.grid(True)
plt.xlabel('theoretical quantiles')
plt.ylabel('sample quantiles')
#%%

# skew and kurtosis

import scipy.stats as scs

data = df['floats'].dropna() # remove missing value
print('skew is %f' %scs.skew(data))
print('skew test p-value is %f' %scs.skewtest(data)[1])
print('kurt is %f' %scs.kurtosis(data))
print('kurt test p-value is %f' % scs.kurtosistest(data)[1])
print('normal test p-value is %f' %scs.normaltest(data)[1])
#%%

