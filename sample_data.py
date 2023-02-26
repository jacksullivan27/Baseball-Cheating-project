#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


def get_ave_spin(col_name, df = pd.read_csv("sample_data.csv")):
    return np.mean(df[col_name])


# In[2]:


# import pandas as pd
# import numpy as np
# test_case = pd.read_csv("sample_data.csv")
# print(get_ave_spin("spin_rate_1", test_case))


# In[3]:


__sample_data__ = []


# In[4]:


def __init__():
    import csv
    """This function will read in the csv_file and store it in a list of dictionaries"""
    __sample_data__.clear()
    with open('sample_data.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            __sample_data__.append(row)


# In[5]:


def count():
    """This function will return the number of records in the dataset"""
    return len(__sample_data__)


# In[6]:


def get_first_name(idx):
    """get_first_name(idx) returns the first name of the player in row idx"""
    return __sample_data__[int(idx)]['first_name']


# In[7]:


def get_last_name(idx):
    """get_last_name(idx) returns the last name of the player in row idx"""
    return __sample_data__[int(idx)]['last_name']


# In[8]:


def get_player_id(idx):
    """get_player_id(idx) returns the id of the player in row idx"""
    return __sample_data__[int(idx)]['player_id']


# In[9]:


__init__()

