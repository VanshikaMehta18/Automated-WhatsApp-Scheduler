#!/usr/bin/env python
# coding: utf-8

# In[1]:


# link your whatsapp web on the browser before using this
import pywhatkit as pwk
import datetime
e=datetime.datetime.now()

pwk.sendwhatmsg('enter phone number here',"Hey! How have you been?",e.hour,e.minute +1) #sends a message to the number, given message, time in 24 hrs, mins 


# In[ ]:




