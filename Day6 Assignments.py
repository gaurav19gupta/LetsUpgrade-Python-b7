#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Assignment 1: Create a bank account that has two attribute ownername,balance and two methods deposit and withdraw.
class account():
    def __init__(self):
        self.ownerName = input("Enter Name:- ")
        self.balance = 0
        
    def deposit(self):
        
        amount = float(input("Enter the amount to be deposited:- "))
        self.balance += amount
        print("Amount Deposited by: " ,self.ownerName, " -", amount)
        print("Balance :-", self.balance)
        
    def withdraw(self):
        amount = float(input("Enter the amount to be withdrawal:- "))
        if(self.balance >= amount):
            self.balance -= amount
            print("Amount Withdrawled by: ",self.ownerName, " -", amount)
            print("Balance :-", self.balance)
        else:
            print("Insufficient Balance")
            
            
        


# In[11]:


shyam = account()


# In[12]:


shyam.deposit()
shyam.withdraw()


# In[ ]:


# Assignment 2 Create a class Cone that has two attribute radius and height and two methods volume and surface area.


# In[7]:


import math

class Cone:
    def __init__(self):
        self.radius = float(input("Enter the radius:- "))
        self.height = float(input("Enter the height:- "))
        
    def volume(self):
        vol = math.pi * self.height * (self.radius**2) * (1/3)
        print("The Volume of Cone:- ", vol)
     
    def surfacearea(self):
        length = math.sqrt(self.radius**2 + self.height**2)
        sa = math.pi * self.radius * length + math.pi *(self.radius**2)
        print("The Surface Area of Cone:- ", sa)


# In[8]:


right_cone = Cone()


# In[9]:


right_cone.volume()
right_cone.surfacearea()


# In[ ]:




