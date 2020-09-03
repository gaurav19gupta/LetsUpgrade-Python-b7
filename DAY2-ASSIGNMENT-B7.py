#!/usr/bin/env python
# coding: utf-8

# In[1]:


#  1.) LIST


# In[2]:


lst =["Gaurav",567,435,"John",50.4]


# In[3]:


lst


# In[4]:


lst.append("Wick")


# In[5]:


lst


# In[6]:


lst.count("Gaurav")


# In[7]:


lst.index(435)


# In[8]:


lst.pop(4)
# pop removes the element at the specified position.


# In[9]:


lst


# In[10]:


lst.reverse()


# In[11]:


lst


# In[13]:


type(lst)


# In[14]:


#  2.) DICTIONARY


# In[15]:


dit = {"name":"Gaurav","age":"20","branch":"CS","number":"123456"}


# In[16]:


dit


# In[17]:


mydit = dit.copy()


# In[18]:


mydit


# In[19]:


dit.keys()


# In[20]:


dit.values()


# In[21]:


dit.get("branch")


# In[22]:


dit.popitem()


# In[23]:


dit


# In[24]:


dit.update({"age":"21"})


# In[25]:


dit


# In[26]:


type(dit)


# In[27]:


# 3.) SETS


# In[28]:


st1 = {"rock","dwayne","johnson","john"}


# In[29]:


st1.add("abrham")


# In[30]:


st1


# In[32]:


st2 = st1.copy()


# In[33]:


st2


# In[34]:


st2.add("rdj")


# In[35]:


st2


# In[36]:


st1.intersection(st2)


# In[37]:


st2.difference(st1)


# In[38]:


st2


# In[39]:


st1.issubset(st2)


# In[40]:


st2.issuperset(st1)


# In[41]:


type(st1)


# In[42]:


# 4.) TUPLE


# In[43]:


tup = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)


# In[44]:


tup.count(5)


# In[45]:


tup.index(7)


# In[46]:


tup[2:]


# In[47]:


tup[2:6]


# In[48]:


tup1 =("iron man","captain america")


# In[49]:


tup + tup1


# In[50]:


type(tup)


# In[51]:


# 5.) STRING


# In[52]:


a = "welcome to python"


# In[53]:


a


# In[54]:


a.capitalize()


# In[56]:


a.count("o")


# In[57]:


a.index("p")


# In[58]:


a.isalpha()


# In[59]:


a.isspace()


# In[60]:


a.title()


# In[61]:


type(a)


# In[ ]:




