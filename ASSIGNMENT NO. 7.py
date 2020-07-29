#!/usr/bin/env python
# coding: utf-8

# In[72]:


#ASSIGNMENT NO. 7
#QUASTION NO. 1

dict = {21:"FTP",22:"SSH",23:"telnet",80:"http"}
print("port1 = ",dict)

dict = {value:key for key, value in dict.items()}
print("prot2 = ",dict)
  


# In[ ]:


#QUASTION NO. 2, I CAN'T UNDERSTAND PLZ EXPLAIN FOR ME 


# In[34]:


#QUASTION NO. 3

l = [(1,2,3),[1,2],['a','hit','less']] 
   
output = []
l = list(itertools.chain(*l))

def reemovNestings(l): 
    for i in l: 
        if type(i) == list: 
            reemovNestings(i) 
        else: 
            output.append(i) 
reemovNestings(l) 
print ('The Final list: ', output) 


# In[28]:





# In[ ]:





# In[ ]:




