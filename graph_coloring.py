#!/usr/bin/env python
# coding: utf-8

# In[10]:


class Graph:
    def __init__(self,vertices):
        self.V=vertices
        #self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]


    def isSafe(self,v,color,c):
        for i in range(self.V):
            if self.graph[v][i] == 1 and color[i]==c:
                return False
        return True
    
    
    def graphUtil(self,m,color,v,solutions):
        if v==self.V:
            solutions.append(list(color))
            return
        for c in range(1,m+1):
            if self.isSafe(v,color,c):
                color[v]=c
                self.graphUtil(m,color,v+1,solutions)
                color[v]=0
                    
    
    def graphColuring(self,m):
        solutions=[]
        color=[0]*self.V
        self.graphUtil(m,color,0,solutions)
        
        if len(solutions) == 0:
            return False
        
        for sol in solutions:
            print(sol)
        
        
if __name__ == '__main__':
    g=Graph(4)
    g.graph=[[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
    m=3
    g.graphColuring(m)


# In[ ]:




