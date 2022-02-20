#!/usr/bin/env python
# coding: utf-8

# In[1]:


# This module shows the effect of multiple imports and reload

print("This code got executed")


# In[2]:


try:
    get_ipython().system('jupyter nbconvert --to python myModel.ipynb')
except:
    pass

