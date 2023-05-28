from heapq import *                                          #importing functions like heappush,heappop from heapq library used to maintain a priority queue

def prims(graph, start, parent,distance, visited):          #parent dictionary store the parent of each node in MST, distance dictionary store the minimum distance from start nde to each node
    bag  = []                                              #priority queue bag is initialised


    heappush(bag, [0,start])                                #start node is added to priority queue with distance 0
    distance[start] = 0                                     #distance of start node is set to 0
    parent[start] = -1                                      #parent of start node is set to -1


    while bag:                                         #code enters a while loop that continues until the priority queue is emty 
        d,n = heappop(bag)                             #in each iteration the node with the smallest distance is extracted from the pq


        if not visited[n]:                            #if the extracted node is not visited then it is marked as visited
            visited[n] = 1
            for cd, cn in graph[n]:                        #code check all the neighbours of the current node

                if distance[cn] > cd and not visited[cn]:       # If the distance to a neighbor is less than its current recorded distance (distance[cn]) and the neighbor has not been visited:
                                                                #The parent of the neighbor is updated to the current node.The distance to the neighbor is updated.
                                                                #The neighbor and its new distance are added to the priority queue.
                    parent[cn] = n
                    distance[cn] = cd
                    heappush(bag, [cd, cn])
    print(distance)
    print(parent)

edges = [[1, 2, 1], [2, 3, 4], [3, 4, 1], [4, 5, 2], [1, 5,3], [2, 5, 2], [2,4,1]]   #Each item in the list consists of three elements: the starting node, the ending node, and the weight of the edge.
n = 5
graph = {}
parent  = {}
distance = {}
visited = {}

for i in range(1, n+1):
    graph[i] = []
    parent[i] = None
    distance[i] = 10**8+1
    visited[i] = 0

for u,v,d in edges:
    graph[u].append([d,v])
    graph[v].append([d,u])

start = 1
prims(graph, start, parent, distance, visited)