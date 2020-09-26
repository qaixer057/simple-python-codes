#!/usr/bin/env python
# coding: utf-8

# In[45]:


import cv2


# In[46]:


img = cv2.imread('target.png', 1)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# In[47]:


import matplotlib.pyplot as plt
plt.imshow(img)


# In[48]:


img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# In[49]:


plt.imshow(img_gray)


# In[50]:


img_invert = cv2.bitwise_not(img_gray)


# In[51]:


plt.imshow(img_invert)


# In[52]:


img_smoothing = cv2.GaussianBlur(img_invert, (21, 21),sigmaX=0, sigmaY=0)


# In[53]:


plt.imshow(img_smoothing)


# In[54]:


def sketch(x, y):
    return cv2.divide(x, 255 - y, scale=256)


# In[55]:


final_img = sketch(img_gray, img_smoothing)


# In[56]:


plt.imshow(final_img)


# In[57]:


# plt.savefig(final_img)
cv2.imwrite('Qaiser_DP.jpg',final_img)


# In[ ]:




