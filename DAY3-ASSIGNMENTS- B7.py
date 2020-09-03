#!/usr/bin/env python
# coding: utf-8

# # Assignment 1 Day3
# 

# In[1]:


altitude = input("Enter the Altitude: ")
altitude = int(altitude)
if altitude <1000:
    print("Safe to Land")
elif altitude <5000:
    print("Bring down to 1000")
else:
    print("Turn Around")


# # Assignment 2 Day3

# In[5]:


for i in range(1,200 + 1):
   if i > 1:
       for j in range(2,i):
           if(i%j) == 0:
               break
       else:
            print(i)

