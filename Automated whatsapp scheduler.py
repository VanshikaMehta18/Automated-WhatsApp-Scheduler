#!/usr/bin/env python
# coding: utf-8

# In[1]:


# link your whatsapp web on the browser before using this
import pywhatkit as pwk
import datetime
e=datetime.datetime.now()

pwk.sendwhatmsg('enter phone number here',"Hey! How have you been?",e.hour,e.minute +1) #sends a message to the number, given message, time in 24 hrs, mins 


# In[8]:


from selenium import webdriver

class infow():
    def __init__(self):
        # Use double backslashes or a raw string for the path
        self.driver = webdriver.Chrome(executable_path=r'D:\chromedriver_win32.exe')
     
    def get_info(self, query):
        self.query = query
        self.driver.get(url="https://www.wikipedia.org")

# Create an instance of the class
assist = infow()

# Call the get_info method
assist.get_info("hello")


# In[ ]:




