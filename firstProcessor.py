
# coding: utf-8

# # Cleaning Energy Game database output (March, 21st, 2018)
# 
# In order to use the output of the energy game for scientific purposes, it is needed to clean the database output. This script shows the process to clean the current database output.

# # 0.Import libraies

# In[1]:

import os
import pandas as pd
import datetime


# ## 1.Import the output of the current version of the database (March, 21st, 2018)

# In[2]:

now = datetime.datetime.now()
slicing = True
from_participant = 4 # If it's needed to request data from a specific person to the lastest record


# In[3]:

db = pd.read_csv('data/data.csv')
db.head()


# ## 2.Import the list of columns relevant for analysis

# In[4]:

columns = pd.read_csv('assets/relevant_cols.txt')

cols = [columns.values[i][0] for i in range(len(columns.values))]
cols


# ## 3.Select columns from the output database and put into csv

# In[5]:

db.iloc[:,cols]


# In[6]:

if slicing:
    db.iloc[from_participant:,cols].to_csv('./energy_game_clean'+str(now.strftime("%Y-%m-%d"))+'.csv')
else:
    db.iloc[:,cols].to_csv('./energy_game_clean'+str(now.strftime("%Y-%m-%d"))+'.csv')


# In[ ]:



