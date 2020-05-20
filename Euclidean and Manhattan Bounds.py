#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing numpy and pandas
import numpy as np
import pandas as pd
import scipy
import math
from scipy.spatial import distance
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# Function for generation of data-points
def point_generation(n,d):
  arr = []
  for i in range(n):
    arr.append([np.random.randn() for j in range(d)])
  return arr


# In[3]:


# Function for generating instances of Euclidean chi
def calculate_euclidean_chi(df):
  # Calculating euclidean distance
  euclidean_distance = scipy.spatial.distance.cdist(df.values,df.values, metric = "euclidean")
  ed = pd.DataFrame(euclidean_distance)
  np.fill_diagonal(ed.values,None)
  euclidean_max = ed.max().max()
  euclidean_min = ed.min().min()
  euclidean_chi = math.log((euclidean_max-euclidean_min)/euclidean_min)
  return euclidean_chi


# In[4]:


# Function for generating instances of Manhattan chi
def calculate_manhattan_chi(df):
  # Calculating manhattan distance
  manhattan_distance = scipy.spatial.distance.cdist(df.values,df.values, metric = "cityblock")
  md = pd.DataFrame(manhattan_distance)
  np.fill_diagonal(md.values,None)
  manhattan_max = md.max().max()
  manhattan_min = md.min().min()
  manhattan_chi = math.log((manhattan_max-manhattan_min)/manhattan_min)
  return manhattan_chi


# In[5]:


# Main function which generates chi values
if __name__ == "__main__":
  n_list = []
  d_list = []
  euclidean_chi_list = []
  manhattan_chi_list = []
  # Iterating for n between 100 to 1000, and d between 1 to 100
  for n in range(100,1001):
    print(n)
    for d in range(1,101):
      # Creating data frame
      df = pd.DataFrame(point_generation(n,d))
      # Calling euclidean chi for df
      euclidean_chi = calculate_euclidean_chi(df)
      manhattan_chi = calculate_manhattan_chi(df)
      n_list.append(n)
      d_list.append(d)
      euclidean_chi_list.append(euclidean_chi)
      manhattan_chi_list.append(manhattan_chi)
  euclidean_manhattan_chi_df = pd.DataFrame(list(zip(n_list,d_list,euclidean_chi_list,manhattan_chi_list)))
  euclidean_manhattan_chi_df.to_csv(r'/Users/advaitiyer/Desktop/Syracuse University/Academics/3rd Semester/Analytical Data Mining CIS 787/Homeworks/HW1/chi_df.csv')


# In[20]:


# Plotting Euclidean distance 
fig = plt.figure()
ax = fig.gca(projection='3d') # Plotting euclidean distance
ax.plot_trisurf(euclidean_chi_list, n_list, d_list, cmap='viridis', edgecolor=None)
plt.show()
plt.savefig("euclidean.png", dpi=100)


# In[19]:


# Plotting Manhattan distance
fig = plt.figure()
mycmap = plt.get_cmap('gist_earth')
ax = fig.gca(projection='3d') # Plotting manhattan distance
ax.plot_trisurf(manhattan_chi_list, n_list, d_list, cmap=mycmap)
plt.show()
plt.savefig("manhattan.png",dpi=100)

