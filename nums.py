#!/usr/bin/env python
# coding: utf-8

# In[17]:


nums=[1,4,8,9]
n= nums[-1]
def ind_missing_nums(nums):
    nums1 = list(range(1,n+1))
    x=[]
    for i in nums1:
        if i not in nums:
            x.append(i)
    print(x)
ind_missing_nums(nums)


# In[ ]:





# In[ ]:




