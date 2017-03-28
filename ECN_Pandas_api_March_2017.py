
# coding: utf-8

# # Presentation outline
# - Purpose and use of Pandas
# - Pandas data structures 
# - Loading data
# - Simple data analysis and exploration 
# - Selecting and indexing 
# - Visualizing 
# - Using APIs - examples 
# - Requests 
# - Scrapy 

# # Purpose of Pandas 
# - Large data sets 
# - Clean up data 
# - Statistical analysis 
# - Presentation 
# - Never use excel again!

# # Get Started
# 

# In[1]:

import pandas as pd
import numpy as np
import datetime as dt


# # Data Structures 
# - Series: One-dimensional array-like object with index. Data any numpy data type 
# - Data frame: Spreadsheet-like data structure with column and row indexes
# 
# 

# ## Series - create from dictionary or list 

# In[2]:

cara_states_dict = {'Arizona':11, 'Ohio':3, 'Oregon':2,'Washington':23, 'Texas':0}
dseries = pd.Series(cara_states_dict)
dseries


# In[3]:

cara_states = ['Arizona', 'Ohio','Oregan','Texas','Washington']
cara_years = [11, 3, 2, 0, 23]
lseries = pd.Series(cara_years, cara_states)
lseries


# ### Some attributes

# In[4]:

dseries.values
#note values are array data type
#dseries.index
#dseries.axes
#dseries.size


# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.html

# ### Some methods 

# In[5]:

dseries.mean()
#dseries.median()
#dseries.mean()
#dseries.sort_values()
#dseries.sort_index()


# ### Selecting

# In[6]:

dseries['Ohio']


# In[7]:

dseries[['Ohio','Oregon']]


# ## Dataframe  - creating 

# In[8]:

datdict = {'state':['Arizona','Oregon','Washington','Ohio'], 
           'year':[2002,1978,1980,2008], 'time':[11,2,23,3]}
df = pd.DataFrame(datdict)
df


# In[9]:

dat = np.random.rand(4,3)
dat
rdf  = pd.DataFrame(dat,columns = ['col1','col2', 'col3'],
                    index = ['a','b','c','d'])
rdf


# ## Dataframe - column selection & values 

# In[10]:

rdf['col3']


# In[11]:

rdf['col3'].values


# # Loading data 
# - Load many types of data to DataFrame 
# http://pandas.pydata.org/pandas-docs/stable/io.html
# 

# In[12]:

pwt = pd.read_csv('pwt90.csv', engine = 'python')
pwt


# ### Get information about DataFrame

# In[13]:

pwt.info()


# ### A closer look

# In[14]:

pwt.country
pwt.country.unique()
#pwt.countrycode.unique()


# ### Selection by row
# -choose the rows of the dataframe that meet criteria using .loc attribute and .isin method 

# In[15]:

countries = ['Paraguay','United States']
mask = pwt['country'].isin(countries)
mask
pwt_revised = pwt.loc[mask]
#pwt_revised
#or
#pwt_revised = pwt.loc[pwt.country.isin(countries)]
#pwt_revised


# In[16]:

mask = (pwt_revised['country'] == 'United States') & (pwt_revised['year'].isin([1960,2004]))
pwt_revised.loc[mask]


# #### Useful selection tools

# - '>', '<', '==', '>=','<='
# - '&', '|'  and, or
# - '~' not
# 

# In[17]:

pwt_not_USA = pwt.loc[~(pwt['country']=='United States')]
#pwt_not_USA
#could be ~ any critera 


# more here http://pandas.pydata.org/pandas-docs/stable/indexing.html

# ### Select by column

# In[18]:

cols = ['country','year','rgdpe','pop','emp','currency_unit']
pwt_abbr = pwt_revised[cols]
pwt_abbr


# ### Create new columns

# In[19]:

pwt_abbr['rgdp_percapita'] = pwt_abbr['rgdpe']/pwt_abbr['pop']
pwt_abbr['rgdp_peremp'] = pwt_abbr['rgdpe']/pwt_abbr['emp']
#or pwt_abbr.loc[:,'rgdp_percapita] = pwt_abbr['rgdpe']/pwt_abbr['pop']
#warnings are ok


# ## Methods and axis 

#  - axis = 0 means apply method down
#  - axis = 1 means apply method across
#  - axis = 0 is (usually) default 

# <img src='axis_dataframe.jpg'>

# ## Drop columns 

# In[20]:

pwt_abbr = pwt_abbr.drop(['currency_unit'],axis = 1)
pwt_abbr


# In[21]:

#.drop(labels, axis=0, level=None, inplace=False, errors='raise')
#default axis = 0
#default is to return a copy, inplace=True overwrites, 
#but raises copy error 


# ### Drop NaN rows

# In[22]:

pwt_drop = pwt_abbr.dropna(inplace = False)
pwt_drop


# ### Interpolate

# In[23]:

pwt_abbr = pwt_abbr.interpolate()
pwt_abbr


# #### Now drop na

# In[24]:

pwt_abbr.dropna(inplace = True)
pwt_abbr


# #### Missing data

# - .dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
#     - how = 'all' drops rows that are all NaN and leaves rows with one Nan
# - .fillna(value=None, method=None, axis=None, inplace=False, limit=None, downcast=None)
#     - http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.fillna.html
# - See also  http://pandas.pydata.org/pandas-docs/stable/missing_data.html

# ## Exploring: maximums, minimums, mean, correlation 

# ### Maximum values 

# In[25]:

maxvals = pwt_abbr.rgdp_percapita.max()
maxvals


# In[26]:

#.max(axis=None, skipna=None, level=None, numeric_only=None, **kwargs)
#releted min, mean, median, mode, var, std 


# ### Where maximum values occur 

# In[27]:

maxloc = pwt_abbr[['rgdp_percapita']].idxmax()
pwt_abbr.loc[maxloc]


# In[28]:

#.idxmax(axis=0, skipna=True)
#related idxmin() 
## Careful! First instance only 


# ### Correlation Coefficients 

# In[29]:

pwt_abbr.corr()


# In[30]:

#related .cov()


# ## Arithmetic : sum, div + - * / 

# ### Sum across columns - make a new column 

# In[31]:

pwt_abbr['Total'] = pwt_abbr.sum(axis = 1)
#Nonesense in this case, but you can do it


# ### Sum across rows

# In[32]:

pwt_abbr.sum()
#again, nonsense


# ## simple arithmetic - first create new dataframe 

# In[33]:

# related -, *, / (sort of) ** (raised to the power)
# divide entire dataframe by column, use df.div()
# df.div(other, axis='columns', level=None, fill_value=None)


# ### Value counts
# - each column is a series, value counts works only on series, not dataframes

# In[34]:

pwt_abbr['country'].value_counts()


# ## Write to file 

# In[35]:

pwt_abbr.to_csv('~/Desktop/pwt_abbr.csv')


# # Recap
# - Series and Dataframes 
# - Loading data
# - Cleaning data 
# - Basic manipulation 
# - Selecting and indexing 

# ### Lots more to learn!
# - Joing dataframes 
# - More datetime 
# - Statistical tools
# - More plotting - matplotlib 
# 

# ### Using APIs

# - Fred API https://research.stlouisfed.org/docs/api/fred/
# - Turn this https://api.stlouisfed.org/fred/series/observations?series_id=GNPCA&api_key=d78410e1e342db6a5bea137fb6c50be8&file_type=json
#     into something we can use.

# - https://github.com/mortada/fredapi

# In[42]:

#My Fred key is saved in fredkey.py
from fredkey import key
from fredapi import Fred
import datetime as dt


# In[40]:

print(key)


# In[43]:

fred = Fred(api_key=key)
#read documentation on https://github.com/mortada/fredapi


# In[44]:

#Search Fred for series - There are way too many!!
search_results = fred.search('Unemployment').T
search_results.info()


# In[46]:


#create a dataframe to save series
agg = pd.DataFrame(index=[], columns=[])
# The first series
s = 'CNP16OV'


# In[47]:

#Retrieve the series information about CNP16OV
series_info = fred.get_series_info(s)
series_info


# In[48]:

#save the time for column use
series_name = series_info.title
series_name


# In[49]:

#Retrieve the data for CNP16OV
get_ipython().magic('pinfo fred.get_series')


# In[50]:

#fred.get_series() returns a Pandas Series
series_dat = fred.get_series(s, observation_start='1960-01-01', observation_end='2016-12-31')
type(series_dat)
#series_dat


# In[51]:

#Convert monthly series to annual
series_dat = series_dat.groupby(pd.TimeGrouper(freq='A')).mean()
series_dat


# In[52]:

#place the CNP16OV in the dataframe 
agg[series_name] = series_dat


# In[53]:

type(agg)


# In[54]:

#created a dataframe with multiple data series
#series to download
#Civilian Noninstitutional Population iCNP16OV
#Civilian Labor Force (CLF16OV)
#Civilian Employment (CE16OV)
aggregate_series = ['CNP16OV', 'CLF16OV', 'CE16OV']
for s in aggregate_series:
    series_info = fred.get_series_info(s)
    series_name = series_info.title
    series_dat = fred.get_series(s, observation_start='1960-01-01')
    series_dat = series_dat.groupby(pd.TimeGrouper(freq='A')).mean()
    agg[series_name] = series_dat
agg


# In[55]:

#we could save this to excel, create a tab "Labor_data"
writer = pd.ExcelWriter('Labor_Force.xlsx')
agg.to_excel(writer, 'Labor_data')


# ### Another API for European data
# http://pandasdmx.readthedocs.io/en/latest/index.html#

# ### Web scraping 
# - if api not available try this https://doc.scrapy.org/en/latest/index.html

# In[ ]:



