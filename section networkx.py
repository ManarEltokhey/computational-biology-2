#!/usr/bin/env python
# coding: utf-8

# In[9]:


import networkx as nx


# In[10]:


G=nx.Graph()
G.add_nodes_from(['a','b','c','d'])
G.add_edges_from([('a','b'),('a','c'),('c','d'),('b','c')])
nx.draw(G,with_labels=True,node_color="red",font_size=20,font_color="yellow")


# In[11]:


G.nodes()


# In[12]:


G.edges()


# In[13]:


G.neighbors('a')


# In[14]:


list(G.neighbors('a'))


# In[15]:


G.has_node('b')


# In[16]:


G.has_edge('b','c')


# In[17]:


G.number_of_nodes()


# In[18]:


G.number_of_edges()


# In[19]:


'a' in G.nodes()


# In[20]:


nx.is_tree(G)


# In[21]:


nx.is_connected(G)


# In[22]:


G.degree('a')


# In[23]:


D=nx.DiGraph()
D.add_nodes_from(['a','b','c','d'])
D.add_edges_from([('a','b'),('a','c'),('c','d'),('b','c')])
nx.draw(D,with_labels=True,node_color="red",font_size=20,font_color="yellow")


# In[24]:


X=nx.Graph()
X.add_edges_from([(1,2),(2,3),(1,3),(3,4)])
nx.draw(X,with_labels=True,node_size=500)


# In[25]:


dict(X.degree())


# In[26]:


nx.to_numpy_matrix(X)


# In[ ]:





# In[ ]:




