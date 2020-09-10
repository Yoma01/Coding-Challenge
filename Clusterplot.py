#!/usr/bin/env python
# coding: utf-8

# In[17]:


#importing libraries
import pandas as p_d
#plotter is for plotting graphs
import matplotlib.pyplot as plotter
#for scaling data
from sklearn.preprocessing import MinMaxScaler
#for clustering by K_means algorithm
from sklearn.cluster import KMeans


# In[18]:


#loading dataset
import pandas as p_d
data=pd.read_csv('https://raw.githubusercontent.com/ACM-Research/Coding-Challenge/master/ClusterPlot.csv')
data


# In[4]:


#plot the dataset
data.plot(kind='scatter',x='V1', y='V2')
plotter.show()


# In[31]:


# dropping the first column since it is not needed
df=data.drop(['Unnamed: 0'], axis=1)


# In[16]:


# scaling the dataset
mms=MinMaxScaler()
mms.fit(df)
new_data=mms.transform(df)


# In[15]:


new_data


# In[21]:


#convert to dataframe
new_data=p_d.DataFrame(new_data, columns=['V1','V2'])
new_data


# In[22]:


#replot after scaling
new_data.plot(kind='scatter', x='V1', y='V2')
plotter.show


# In[27]:


#elbow method to minimize wss
SOD = []
p_r = range(1,15)
for i in p_r:
    km = KMeans(n_clusters=i)
    km = km.fit(new_data)
    SOD.append(km.inertia_)


# In[30]:


#plotting the elbow curve
plotter.plot(p_r, SOD,'bx-')
plotter.xlabel('k')
plotter.ylabel('Sum of squared dist')
plotter.title('Elbow Method For Optimal k')
plotter.show()


# In[ ]:


# the elbow is at k=3 indicating that the optical number of cluster is 3

