#!/usr/bin/env python
# coding: utf-8

# # 3.2.6生成器
# 生成器是构造新的可遍历对象的一种非常简洁的方式。

# In[2]:


def squares(n=10):
    print('Generating squares from 1 to {0}'.format(n**2))
    for i in range(1,n+1):
        yield i**2


# In[3]:


gen=squares()
gen


# In[6]:


for x in gen:
    print(x,end=' ')


# In[5]:


for x in gen:
    print(x,end=' ')


# In[7]:


for x in gen:
    print(x)


# ## 3.2.6.1生成器表达式
# 用生成器表达式来创建生成器更为简单。创建一个生成器表达式，只需要将列表推导式中的中括号替换为小括号即可。

# In[8]:


gen=(x**2 for x in range(100))
gen


# In[9]:


def _make_gen():
    for x in range(100):
        yield x**2
gen=_make_gen()
    


# In[11]:


sum(x**2 for x in range(100))


# In[12]:


dict((i,i**2) for i in range(5))


# In[ ]:




