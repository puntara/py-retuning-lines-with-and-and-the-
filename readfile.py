#!/usr/bin/env python
# coding: utf-8

# In[19]:


fhand= open('Pride and Prejudice.txt','r')
line_list=list()
for line in fhand:
    line= line.rstrip()
    if  (line.find('The')==-1) and (line.find('the ')==-1) and(line.find('and') ==-1) and (line.find('AND') ==-1):
        continue
    line_list.append(line)
print(line_list[:10])


# In[ ]:




