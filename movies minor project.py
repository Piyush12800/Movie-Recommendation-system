#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib as mlt
import seaborn as sns


# In[51]:


df=pd.read_csv(r'tmdb_5000_movies.csv') 
# df2=pd.read_csv(r'C:\Users\ASUS\Downloads\tmdb_5000_credits.csv')


# In[27]:


# df=pd.merge(df1,df2,on='movie_id')


# In[52]:


df.head()


# In[53]:


print(df.isna().sum())
print("shape:",df.shape)


# In[56]:


df.columns = ['budget','genres', 'homepage', 'movie_id', 'keywords','original_language', 'original_title', 'overview', 'popularity', 'production_companies', 'production_countries', 'release_date','revenue', 'runtime','spoken_languages','status','tagline', 'title', 'vote_average','vote_count'] 
df.drop(columns=['budget','original_language','release_date','spoken_languages','status','tagline','vote_count'],inplace=True)
df.head()


# In[ ]:




