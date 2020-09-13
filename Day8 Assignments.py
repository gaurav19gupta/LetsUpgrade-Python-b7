#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Assignment 1 Day8

def getInput(calculate_arg_fun):
    def Fibonacci(n):
        if n<=0:
            print("Incorrect input")
    # First Fibonacci number is 0
        elif n==1:
            return 0
    # Second Fibonacci number is 1
        elif n==2:
            return 1
        else:
            return Fibonacci(n-1)+Fibonacci(n-2)
        return calculate_arg_fun(a)
    return Fibonacci
        


# In[11]:


@getInput
def fibo(n):
    print(n,"")


# In[12]:


fibo(10)


# In[13]:


#Assignment 2 Day 8
try:
   file = open("letsupgrade.txt","r")
   file.write("This is my test file for exception handling!!")
except IOError:
   print("Error: can\'t find file or read data")
else:
   print("Written content in the file successfully")


# In[ ]:




