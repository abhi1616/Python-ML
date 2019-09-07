#!/usr/bin/env python
# coding: utf-8

# In[155]:


pip install requests


# In[156]:


import urllib.request
from bs4 import BeautifulSoup as BS


# In[157]:


data_url = "https://www.iiitm.ac.in/index.php/en/alumini/alumini-our-pride"


# In[158]:


page = urllib.request.urlopen(data_url)


# In[159]:


soup = BS(page)


# In[160]:


print(soup.title.string)


# In[161]:


all_links = soup.find_all("a")


# In[162]:


all_tables = soup.find_all("table")


# In[163]:


list = []

for row in all_tables:
    cells = row.findAll("p")
    for p in cells:
        #print(p.string)
        list.append(p.string.split("\n"))
        #print(list)


# In[164]:


A = []
B = []
C = []
D = []

for i in range(int(len(list)/3) - 1):
    A.append(i+1)
    
for i in range(3, len(list) -2, 3 ) :
    B.append(list[i])
    C.append(list[i+1])
    D.append(list[i+2])


# In[165]:


import pandas as pd
import numpy as np

df = pd.DataFrame(A, columns = ["Number"])
df["Name of Alumni"] = np.array(B)
df["Designation"] = np.array(C)
df["Name of the Company"] = np.array(D)
df

