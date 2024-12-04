#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json


# In[3]:


def save_json(data, filepath):
    """
    save data to a json file
    """
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)


# In[5]:


def load_json(data, filepath):
    """
    save data to a json file
    """
    with open(filepath, "r") as f:
        return json.load(f)

