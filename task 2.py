#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cobra
from cobra import Model,Reaction,Metabolite
model=Model("model 2")
v0=Reaction("v0")
v0.name="v0"
v0.lower_bound=1
v0.upper_bound=1
v1=Reaction("v1")
v1.name="v1"
v1.lower_bound=0
v1.upper_bound=1000
v2=Reaction("v2")
v2.name="v2"
v2.lower_bound=0
v2.upper_bound=1000
v3=Reaction("v3")
v3.name="v3"
v3.lower_bound=0
v3.upper_bound=1000
glc=Metabolite("glc",compartment="c")
AA=Metabolite("AA",compartment="c")
biomass=Metabolite("biomass",compartment="c")
v0.add_metabolites({glc:1})
v1.add_metabolites({glc:-1,AA:1})
v2.add_metabolites({AA:-9.09,biomass:1})
v3.add_metabolites({biomass:-1})
model.add_reactions([v0,v1,v2,v3])
model.objective="v3"
model.optimize()


# In[9]:


cobra.io.save_json_model(model,"E:/abdo/task2.json")


# In[10]:


import escher
from escher import Builder
cobra.io.load_json_model("task2.json")
builder=Builder()
builder


# In[ ]:





# In[ ]:




