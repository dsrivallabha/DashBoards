#!/usr/bin/env python
# coding: utf-8

# In[1]:


import panel as pn 


# In[2]:


pn.extension()


# # Checking float inputs

# In[3]:


current = pn.widgets.FloatInput(name='Current', value=5., step=1e-1, start=0, end=1000, width=100, margin=(10, 5, 5, 10))
#current


# In[4]:


voltage = pn.widgets.FloatInput(name='Voltage', value=220., step=1e-1, start=0, end=1000, width=100, margin=(10, 5, 5, 10))
#voltage


# In[5]:


def resistance(voltage, current):
    return """
              Current is {} Amperes \n
              Voltage value is Volts {} \n
              Resistance is {:.3f} Ohms
            """.format(current, voltage, voltage/current)


# # Checking binding of two functions 

# In[6]:


bind2_fn = pn.bind(resistance, voltage=voltage, current=current)
#bind2_fn()


# # Adding images

# In[7]:


voltage_pane = pn.pane.PNG('./images/VoltageSource.png', width=100)
#voltage_pane


# In[8]:


current_pane = pn.pane.PNG('./images/Current.png', width=100)
#current_pane


# In[9]:


VoltPI = pn.Column(voltage_pane, voltage, background='#f0f0f0')
#VoltPI


# In[10]:


CurrPI = pn.Column(current_pane, current, background='#f0f0f1')
#CurrPI


# In[11]:


resistance_pane = pn.pane.PNG('./images/Resistance.png', width=50)
#resistance_pane


# In[12]:


ResPI = pn.Row(resistance_pane, bind2_fn, background='#f0f0f9')
#ResPI


# In[13]:


Spacing = pn.pane.HTML(background='#FFFFFF', width=100, height=100)
Part1 = pn.Column(VoltPI,  CurrPI)
Part2 = pn.Column(Spacing, ResPI)
Part3 = pn.Row(Part1, pn.Spacer(width=10), Part2)


# In[14]:


Part3.show()


# In[ ]:




