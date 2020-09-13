#!/usr/bin/env python
# coding: utf-8

# # Day9 Assignment1 

# In[9]:


get_ipython().run_cell_magic('writefile', 'primecheck.py', '\'\'\'\nmethod to check number is prime or not\n\'\'\'\ndef prime(num):\n    \'\'\'\n    Base case\n    \'\'\'\n    if num <= 1:\n        return False\n    \'\'\'\n    check for number in 2 to n-1\n    \'\'\'\n    for i in range(2, num):\n        if num%i == 0:\n            return "It is not a prime number"\n    return "It is a prime number"')


# In[10]:


get_ipython().system(' pylint "primecheck.py"')


# In[31]:


get_ipython().run_cell_magic('writefile', 'testprime.py', '# pylint: disable=missing-module-docstring\n# pylint: disable=missing-class-docstring\n# pylint: disable=missing-function-docstring\n\nimport unittest\nimport primecheck\nclass TEST(unittest.TestCase):\n    def test_is_five_prime(self):\n        """Is five successfully determined to be prime?"""\n        num = 5\n        result = primecheck.prime(num)\n        self.assertTrue(result, 5)\n\nif __name__ == \'__main__\':\n    unittest.main()')


# In[32]:


get_ipython().system(' pylint testprime.py')


# # Day9 Assignment 2
# 

# In[55]:


lst = list(range(1000)) 
def armstrongcheckGen(lst):  
    for num in lst:  
        sum = 0  
        temp = num  
        while temp > 0:  
            digit = temp % 10  
            sum += digit ** 3  
            temp //= 10 
        if num == sum:  
            yield num 


# In[57]:


print(list(armstrongcheckGen(lst)))

