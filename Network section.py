#!/usr/bin/env python
# coding: utf-8

# In[6]:


import networkx as nx


# In[7]:


G=nx.Graph()
G.add_nodes_from(['a','b','c','d'])
G.add_edges_from([('a','b'),('a','c'),('c','d'),('b','c')])
nx.draw(G,with_labels=True,node_color="red",font_size=20,font_color="yellow")


# In[8]:


G.nodes()


# In[9]:


G.edges()


# In[10]:


G.neighbors('a')


# In[13]:


list(G.neighbors('a'))


# In[14]:


G.has_node('b')


# In[16]:


G.has_edge('b','c')


# In[17]:


G.number_of_nodes()


# In[18]:


G.number_of_edges()


# In[20]:


'a' in G.nodes()


# In[21]:


nx.is_tree(G)


# In[22]:


nx.is_connected(G)


# In[23]:


G.degree('a')


# In[24]:


D=nx.DiGraph()
D.add_nodes_from(['a','b','c','d'])
D.add_edges_from([('a','b'),('a','c'),('c','d'),('b','c')])
nx.draw(D,with_labels=True,node_color="red",font_size=20,font_color="yellow")


# In[ ]:




