#!/usr/bin/env python
# coding: utf-8

# In[17]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime as dt
import math


# In[28]:


A=np.array([[1,2,3],[4,5,6]])
print(A)

Af=np.array([1,2,3],float)
print(Af)


# In[30]:


a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
print(d[0])


# In[27]:


print(np.arange(0,1,0.2))

np.linspace(0,2*np.pi,10)


# In[4]:


xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.show()


# In[5]:


x=[1,2,3,4,5,6,7,8,9]
y=[1,2,3,4,5,6,7,8,9]
xarr=np.array(x)
yarr=np.array(y)
x33=xarr.reshape(3,3)
y33=yarr.reshape(3,3)
print('list reshaped to array: \n')
print(x33)
print('product of the two matrices is : \n')
product=np.matmul(x33,y33)
print(product)


# In[6]:


arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x)


# In[7]:


spreadsheet = pd.read_csv('C:/Users/ANIRBAN/Downloads/archive/Temperature_And_Precipitation_Cities_IN/Chennai_1990_2022_Madras.csv')


# In[8]:


spreadsheet.head()


# In[9]:


plt.rcParams["figure.figsize"] = [15.00, 7.50]
plt.rcParams["figure.autolayout"] = True
columns = ["time", "prcp"]
arr=spreadsheet.values
print(arr)
plt.plot(spreadsheet.time, spreadsheet.prcp)
plt.show()


# In[10]:


nparr=np.array(arr)


# In[11]:


timedat=nparr[:,0]
prcpdat=nparr[:, 4]
print(prcpdat)
print(len(prcpdat))
newtime=timedat[0:31]
newprcp = prcpdat[0:31]
plt.plot(newtime, newprcp)
plt.show()


# In[12]:


from scipy.integrate import odeint


def model(y,t):
    k = 0.3
    dydt = -k * y
    return dydt

# initial condition
y0 = 5

# time points
t = np.linspace(0,20)

# solve ODE
y = odeint(model,y0,t)

# plot results
plt.plot(t,y)
plt.xlabel('time')
plt.ylabel('y(t)')
plt.show()


# In[26]:


from scipy.integrate import odeint


def model(y,t):
    g=9.8
    l=0.5
    k=g/l;
    return (y[1],-k*y[0])

# initial condition
y0 = [(math.pi)/15,0]

# time points
t = np.linspace(0,10,1000)

# solve ODE
y = odeint(model,y0,t)

# plot results
plt.plot(t,y)
plt.xlabel('time')
plt.ylabel('y(t)')
plt.show()


# In[39]:


from scipy import misc
import imageio
f = misc.face()
imageio.imsave('face.png', f) # uses the Image module (PIL)
import matplotlib.pyplot as plt
plt.imshow(f)
plt.show()


# In[38]:


from PIL import Image as PImage
im = PImage.open('C:/Users/ANIRBAN/Downloads/spm_3dprint.jpeg')
plt.imshow(im)
plt.show()


# In[43]:


f = misc.face(gray=True)
plt.imshow(f, cmap=plt.cm.gray)


# In[49]:


img = np.mean(im, axis=2)
plt.imshow(img)
plt.show()


# In[53]:


from PIL import Image
img2 = Image.open('C:/Users/ANIRBAN/Downloads/spm_3dprint.jpeg').convert('L')
img2.save('pil-greyscale.png')
plt.imshow(img2)
plt.show()


# In[74]:


face = misc.face(gray=True)
print(face)
len(face)
print(face[0])


# In[ ]:




