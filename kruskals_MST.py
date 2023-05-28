def find(graph , node):                            #used to find out the representative root element of the node
    if graph[node]<0:
        return node
    else:
        tmp  = find(graph, graph[node])
        graph[node] = tmp
        return tmp
  
def union(graph, a, b, answer):                 #used to check if no cycles are there
    ta = a 
    tb = b
    a = find(graph, a)                         #used to merge two sets 
    b = find(graph, b)
    if a == b:                          #If the representatives of a and b are the same, it means both nodes are already in the same set, so no further action is taken.
        pass
    else :
        answer.append([ta, tb])                    #no cycles are formed so we can append it in our solution


        if graph[a]<graph[b]:                         #then a becomes the parent of b, and the size of set a is updated accordingly.
            graph[a] = graph[a] +graph[b] 
            graph[b] = a
        else:                                      # Otherwise, b becomes the parent of a, and the size of set b is updated.

            graph[b] = graph[a] + graph[b]
            graph[a] = b

# edges  =  [[1,2,3], [2, 3, 2], [2, 5,1], [3, 4,4], [4,5,8],
#            [3,7,4], [4,7,5], [5, 6, 6], [7, 6, 2], [7, 8, 1],
#            [7, 9, 2], [6, 9, 1]]
# n = 9

edges  = [[1,2,1], [1, 3, 3], [2, 6, 4], [3, 6, 2], [3, 4, 1], [4, 5, 5],
          [6, 7, 2], [6, 5, 6], [7, 5, 7]]
n = 7
answer = []
edges  = sorted(edges, key = lambda edges:edges[2])                                                        
print(edges)
graph = [-1] * (n+1)                             #initialized with -1

for u,v,d in edges:                          #function is called to merge the sets containing nodes u and v into a single set.
    union(graph, u, v, answer)       # This step ensures that only the edges that do not create cycles are added to the MST.

for item in answer:    
    print(item)
