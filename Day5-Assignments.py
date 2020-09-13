#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Assignment 1 Day5
# Q1 To identify sublist given in the list in the same order.


# In[2]:


lst =[1,5,6,4,1,2,3,5]
sub =[1,1,5]
count,j = 0,0 

for i in sub:
    while j<len(lst):
        if lst[j]==i:
            j+=1
            count+=1
            print(count,j)
            break
        j+=1
        
if count == len(sub):
    print("It's a match")
else:
    print("it's Gone")


# In[ ]:


# Assignment2 Day5


# In[3]:


def is_prime(n): 
    if n <= 1: 
        return False
    for i in range(2,n): 
        if n % i == 0: 
            return False
    return True


# In[4]:


lst = list(range(2500))


# In[5]:


lst_prime = filter(is_prime,lst)
print(list(lst_prime))


# In[ ]:


# Assignment 3 Day5


# In[6]:


lst =["hey this is sai","i am in mumbai"]
lst_arg = map(lambda x: x.title(),lst)
print(list(lst_arg))

