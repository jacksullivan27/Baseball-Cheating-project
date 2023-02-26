#!/usr/bin/env python
# coding: utf-8

# In[1]:


def get_ave_diff(col_name, df):
    return np.mean(df[col_name])


# In[6]:


import pandas as pd
import numpy as np
cheating_case = pd.read_csv("curve_diff.csv")
cheating_case = cheating_case[cheating_case["spin_diff"] > 0]


# In[3]:


__curve_diff__ = []


# In[4]:


def __init__():
    import csv
    """This function will read in the csv_file and store it in a list of dictionaries"""
    __curve_diff__.clear()
    with open('curve_diff.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            __curve_diff__.append(row)


# In[5]:


def count():
    """This function will return the number of records in the dataset"""
    return len(__curve_diff__)


# In[5]:


def get_first_name(idx):
    """get_first_name(idx) returns the first name of the player in row idx"""
    return __curve_diff__[int(idx)][' first_name_2020']


# In[4]:


def get_last_name(idx):
    """get_last_name(idx) returns the last name of the player in row idx"""
    return __curve_diff__[int(idx)]['last_name_2020']


# In[8]:


def get_player_id(idx):
    """get_player_id(idx) returns the id of the player in row idx"""
    return __curve_diff__[int(idx)]['player_id']


# In[9]:


def get_spin_2020(idx):
    """get_spin_2020(idx) returns the spin difference in 2020 of the player in row idx"""
    return __curve_diff__[int(idx)]['spin_rate_2020']


# In[10]:


def get_spin_2021(idx):
    """get_spin_2021(idx) returns the spin difference in 2021 of the player in row idx"""
    return __curve_diff__[int(idx)]['spin_rate_2021']


# In[2]:


def get_valid_spin(first_name, last_name):

    for idx in range(count()):
        if get_first_name(idx) == first_name:
            if get_last_name(idx) == last_name:
                return float(get_spin_2021(idx))


# In[12]:


__init__()

