#!/usr/bin/env python
# coding: utf-8

# In[106]:


import pandas as pd
tatinc =pd.read_csv("titanic_train.csv")


# In[3]:


df


# ### 1. size of the data

# In[4]:


df.shape


# In[41]:


3*3


# In[6]:


891*12


# In[5]:


df.size


# In[8]:


df.memory_usage(deep=True)


# # 2. how the data looks likes

# In[20]:


df.head()


# In[10]:


df.tail()


# In[16]:


df.sample(5)


# # 3. what are the dtype of col

# In[21]:


df.dtypes


# In[22]:


df.info()


# # 4. how data looks like mathematically

# In[24]:


df.describe().T


# # 5. check missing value

# In[25]:


df.isnull()


# In[26]:


df.isnull().sum()


# In[27]:


df.isnull().sum().sum()


# #  duplilcated value

# In[29]:


df.duplicated().sum()


# In[30]:


df[df.duplicated()]


# # check the unique value

# In[31]:


df.nunique()


# In[37]:


corr_mat=df.corr()


# In[38]:


import seaborn as sns


# sns.heatmap(corr_mat,annot=True)

# # univaritae analysis
# # bivariate analysis
# # multivariate analysis

# In[61]:


df.head(50)


# In[47]:


df.columns


# In[ ]:


### categoical variale
### numeric variable


# In[54]:


cat_feature=[column for column in df.columns if df[column].dtype=="O"]


# In[55]:


num_feature=[column for column in df.columns if df[column].dtype!="O"]


# In[56]:


df[cat_feature]


# In[57]:


df[num_feature]


# # categorical column

# # 1. count plot

# In[58]:


sns.countplot(df["Embarked"])


# In[59]:


sns.countplot(df["Sex"])


# In[60]:


sns.countplot(df["Pclass"])


# In[65]:


df["Sex"].value_counts().plot(kind='bar')


# # 2. pie chart

# In[70]:


df["Sex"].value_counts().plot(kind="pie",autopct='%.2f')


# In[71]:


df["Pclass"].value_counts().plot(kind="pie",autopct='%.2f')


# # numerical column

# # 1. histogram

# In[72]:


import matplotlib.pyplot as plt


# In[73]:


plt.hist(df["Age"])


# In[75]:


plt.hist(df["Age"],bins=5)


# In[76]:


plt.hist(df["Age"],bins=20)


# # Distplot

# In[74]:


sns.distplot(df["Age"])


# # Boxplot

# In[77]:


sns.boxplot(df["Age"])


# In[80]:


df["Age"].min()


# In[81]:


df["Age"].max()


# In[82]:


df["Age"].mean()


# In[84]:


df["Age"].median()


# In[88]:


df["Age"].skew()


# In[89]:


1-0.38910778230082704


# # Bivariate analysis

# In[ ]:


categorical
numerical 


# In[ ]:


X-> categorical Y-> categorical

X-> numerical   Y-> numeircal

X-> catgorical  Y-> numerical


# # Mulvariate analysis
# 
# #### here more than 2 column(3,4,5,6,7...n) will be involed 

# In[91]:


tips=sns.load_dataset("tips")


# In[93]:


flight=sns.load_dataset("flights")


# In[95]:


iris=sns.load_dataset("iris")


# # 1. scatter plot (X-> numeric variable y-> nummeric variable)

# In[97]:


tips


# In[104]:


sns.scatterplot(tips["total_bill"],tips["tip"],hue=tips["sex"],style=tips["smoker"])


# # 2. bar plot (X-> numeric variable y-> categorical variable)

# In[108]:


sns.barplot(tatinc["Pclass"],tatinc["Age"],hue=tatinc["Sex"])


# In[110]:


tatinc.head(2)


# # 2. box plot (X-> numeric variable y-> categorical variable)

# In[111]:


sns.boxplot(tatinc["Sex"],tatinc["Age"],hue=tatinc["Survived"])


# In[118]:


tatinc[tatinc["Survived"]==0]["Age"].max()


# In[119]:


tatinc[tatinc["Survived"]==0]["Age"].min()


# In[120]:


tatinc[tatinc["Survived"]==1]["Age"].max()


# In[121]:


tatinc[tatinc["Survived"]==1]["Age"].min()


# In[124]:


sns.distplot(tatinc[tatinc["Survived"]==0]["Age"],hist=False)
sns.distplot(tatinc[tatinc["Survived"]==1]["Age"],hist=False)


# # heatmap plot (X-> categoricla variable y-> categorical variable)

# In[126]:


tatinc.head()


# In[127]:


tatinc["Pclass"]


# In[130]:


tatinc["Survived"]


# In[131]:


pd.crosstab(tatinc["Pclass"],tatinc["Survived"])


# In[133]:


sns.heatmap(pd.crosstab(tatinc["Pclass"],tatinc["Survived"]),annot=True)


# In[134]:


iris.head()


# In[136]:


sns.pairplot(iris,hue="species")


# # Lineplot()

# In[137]:


sns.lineplot(tips["total_bill"],tips["tip"])


# In[138]:


sns.scatterplot(tips["total_bill"],tips["tip"])


# In[139]:


flight


# In[144]:


flight_new=flight.groupby("year").sum().reset_index()


# In[140]:


sns.lineplot(flight["month"],flight["passengers"])


# In[145]:


sns.lineplot(flight_new["year"],flight_new["passengers"])


# In[150]:


flight.pivot_table(values="passengers",index="month",columns="year")


# In[155]:


plt.figure(figsize=(15,15))
sns.heatmap(flight.pivot_table(values="passengers",index="month",columns="year"),annot=True)


# In[156]:


from pandas_profiling import ProfileReport


# In[157]:


profile=ProfileReport(tatinc,title="pandas profiling report")


# In[158]:


profile.to_file("your_report.html")


# In[159]:


sns.clustermap(flight.pivot_table(values="passengers",index="month",columns="year"),annot=True)


# In[ ]:




