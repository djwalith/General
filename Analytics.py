#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import datetime


# In[21]:


df = pd.read_excel('elspot-prices_2021_hourly_eur.xlsx', index_col='Date')
#dfcap= pd.read_excel('elspot-capacities-no_2021_hourly.xlsx',index_col='Date')


# In[22]:


import os
os.getcwd()


# In[27]:


df.columns


# In[24]:


df.isnull().sum()
df = df.apply(lambda x: x.fillna(x.mean()))


# In[25]:


df1 = df[["SE1","SYS"]]
df2 = df[["SE4","SYS"]]


# In[28]:


import matplotlib.pyplot as plt

ax = df[['Cap_NO2A > DE','Flow_NO2 > DE']].plot()
#ax = df2.plot()
#ax = df.plot(y='SE1'sharex= True, sharey= True)


#plt.plot(x='Date',y='SE1')
#plt.plot(y='SYS')
#plt.legend(loc='best')
#plt.show()
# Additional customizations
#ax.set_xlabel('Date');
ax.legend(fontsize=12)


# In[32]:


import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(4, 4))
sns.heatmap(df[['Cap_NO2A > DE','Flow_NO2 > DE','DE-LU','Kr.sand']].corr(),vmin=-1, vmax=1, annot=True)


# In[34]:


plt.figure(figsize=(42, 42))
sns.lineplot(data=df[['DE-LU','Flow_NO2 > DE']])


# In[182]:


df.Date.dtypes


# In[94]:


dfhour = pd.read_excel('elspot-prices_2021_hourly_eur.xlsx', index_col=1)


# In[97]:


dfhour.Date


# In[75]:


dfhour.corr()


# In[278]:


size = len(dfhour.columns)
ax=plt.figure(figsize=(4, 4))
sns.heatmap(dfhour[['SYS','DE-LU','Kr.sand']].corr(),annot=True, linewidth =0.2)


# In[279]:


size = len(dfhour.columns)
plt.subplots(figsize=(size, size))
sns.boxplot(data=df[['SYS','Oslo','Kr.sand','DE-LU']],width=0.5)


# In[280]:


size = len(dfhour.columns)
plt.subplots(figsize=(size, size))
sns.boxplot(data=dfhour[['DE-LU','Kr.sand']])


# In[281]:


dfhour.dtypes


# In[ ]:
plt.figure(figsize=(4, 4))
sns.heatmap(df2019[['SYS','DE-LU','Kr.sand','Oslo','Bergen','Tromsø','Tr.heim','SE1','SE2','SE3','SE4','FI','EE','LV','LT','DK1','DK2']].corr(),vmin=-1, vmax=1, annot=True)
plt.yticks(rotation=0)

plt.figure(figsize=(40, 40))
chart = sns.heatmap(df1.corr(),vmin=-1, vmax=1, annot=True)
chart.set_xticklabels(chart.get_xticklabels(), rotation=45, horizontalalignment='right')
chart.set_yticklabels(chart.get_yticklabels(), rotation=0)

df1= df[['SE3','SE4','Wind_SE3','Wind_SE4']]
ax = df1[df1.index.month== 2].plot()

df2= df2020[['Kr.sand','Oslo','Bergen','Tromsø','Tr.heim']]
(df1[df1.index.month== 4]>100).sum()

df2018 = pd.read_excel('2018.xlsx', index_col=0)

df2019 = pd.read_excel('2019.xlsx', index_col=0)

df2020 = pd.read_excel('2020.xlsx', index_col=0)

df2021 = pd.read_excel('2021.xlsx', index_col=0)

df2022 = pd.read_excel('2022.xlsx', index_col=0)

df= pd.concat([df2018, df2019, df2020, df2021, df2022])

df2022['Date'] = pd.to_datetime(df2022['Date'], format='%d-%m-%Y')

df['Tr.heim'].min()
df['Tr.heim'].idxmin()

(df_SE[df_SE.index.month== 7]).max()
(df_SE[df_SE.index.month== 7]).idxmax()

import numpy as np
import pandas as pd
import matplotlib.cbook as cbook
import matplotlib.image as image
import matplotlib.pyplot as plt

df1=df[['SYS','DE-LU']]
with open('NordPool.png','rb') as file:
    im = image.imread(file)

fig, ax = plt.subplots()

ax.plot(df['DE-LU'], alpha=0.7, label='Daily German DA Prices')
ax.plot(df['SYS'], alpha=0.7, label='Daily SYS Prices')
ax.grid()
ax.set_ylabel('Eur/MWh')
ax.set_xlabel('Date')

fig.figimage(im, 1400,700, zorder=3, alpha=.3)
fig.legend()

plt.show()

df = pd.concat([df2020,df2021,df2022])
df1['2021-09-11':'2022-09-12']

size = len(df.columns)
plt.subplots(figsize=(size, size))
sns.lineplot(data=df)
plt.ylabel('Eur/MWh')
plt.figimage(im, 3000,1400, zorder=100, alpha=0.8)
plt.legend()
plt.xticks(rotation=0)

#Apply function uses lambda function to each element of the DataFrame, creating a DataFrame of boolean values where True indicates a negative value.
df.apply(lambda x: x<0).sum()

df.apply(lambda x: x<0).groupby(df.index.year).sum()

zerohour = dfhour.apply(lambda x: x==0).groupby(dfhour.index.year).sum()
ax = zerohour.plot(kind='bar', stacked=False)
ax.set_xlabel('Year')
ax.set_ylabel('Count of hours with Zero Prices')
ax.set_title('Count of hours with Zero Prices per Year and per BZA')
ax.legend(title='BZA')
ax.imshow(im, aspect='auto', extent=ax.get_xlim() + ax.get_ylim(), zorder=-1, alpha= 0.1)
plt.show()

ax = sns.boxplot(data=df2022,width=0.5)
ax.set_xlabel('BZA')
ax.set_ylabel('Eur/MWh')
ax.set_title('BoxPlots for Variation of prices')
#ax.legend(title='BZA')
ax.imshow(im, aspect='auto', extent=ax.get_xlim() + ax.get_ylim(), zorder=-1, alpha= 0.1)
plt.show()