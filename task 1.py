#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cobra
from cobra import Model,Reaction,Metabolite
model=Model("task1")
v1=Reaction("v1")
v1.name=v1
v1.upper_bound=1000
v1.lower_bound=0
v2=Reaction("v2")
v2.name=v2
v2.upper_bound=1000
v2.lower_bound=0
v0=Reaction("v0")
v0.name=v0
v0.upper_bound=30
v0.lower_bound=30
R=Reaction("R")
R.name=R
R.upper_bound=1000
R.lower_bound=0
v3=Reaction("v3")
v3.name=v3
v3.upper_bound=18
v3.lower_bound=18
v4=Reaction("v4")
v4.name=v4
v4.upper_bound=1000
v4.lower_bound=0
X=Metabolite("X",compartment="c")
Y=Metabolite("Y",compartment="c")
Z=Metabolite("Z",compartment="c")
ATP=Metabolite("ATP",compartment="c")
v1.add_metabolites({X:-1,Y:1})
v2.add_metabolites({Y:-1,Z:1})
v0.add_metabolites({X:1})
R.add_metabolites({Z:-1})
v3.add_metabolites({X:-1,ATP:1})
v4.add_metabolites({ATP:-1})
model.add_reactions([v0,v1,v2,v3,v4,R])
model.objective=R
model.optimize()



# In[ ]:





# In[ ]:




