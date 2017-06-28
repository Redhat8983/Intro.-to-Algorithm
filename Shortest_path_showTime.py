'''
Created on Dec 3, 2015

@author: Chih-Feng Yu, Yung Chi Liu
'''
from __future__ import print_function
import time,random
import dis

# Initialize two different data structures of graph: Dictionary , Matrix
def iniVal(nodes):
    INF=float("inf")
    weightList = [i for i in range(1,10)]
    for i in range(10):
        weightList.append(INF)

    Graph_dic = {}
    Graph_matrix = [[0 for x in range(nodes)] for x in range(nodes)] 
    for i in range(nodes):
        Graph_dic[i+1]={}
        for j in range(nodes):
            if i == j:
                Graph_matrix[i][j] = 0
                Graph_dic[i+1][j+1]=0
            else:    
                Graph_matrix[i][j] = random.choice(weightList)
                if (Graph_matrix[i][j] != INF):
                    Graph_dic[i+1][j+1]=Graph_matrix[i][j]      
#             print (Graph_matrix[i][j],",", end = "")
#         print ("\n")   
#     print("{\n" + "\n".join("{}: {}".format(k, v) for k, v in Graph_dic.items()) + "\n}")
    
    return (Graph_matrix,Graph_dic)
    
#################################################################
def Dijkstra_Dic(G,source,INF=float("inf")):
    
    dicGraph = G
    visitSet = set()
    minv = source
    
    
    dis = dict((k,INF) for k in dicGraph.keys())
    dis[source] = 0
    
    while len(visitSet)<len(dicGraph):
        visitSet.add(minv)                                  
        for w in dicGraph[minv]:                              
            if dis[minv] + dicGraph[minv][w] < dis[w]:        
                dis[w] = dis[minv] + dicGraph[minv][w]         
        
        new = INF                                     
        for v in dis.keys():
            if v in visitSet: continue
            if dis[v] < new: 
                new = dis[v]
                minv = v
    return dis

#################################################################
def getEdges(G):
    
    v1 = []          
    v2 = []     
    w  = []     
    for i in G:
        for j in G[i]:
            if G[i][j] != 0:
                w.append(G[i][j])
                v1.append(i)
                v2.append(j)
    return v1,v2,w
#################################################################
def BellmanFord_Dic(G, source, INF=float("inf")):
    dicGraph = G
    v1,v2,w = getEdges(dicGraph)
    
    
    dis = dict((k,INF) for k in dicGraph.keys())
    dis[source] = 0

    
    for k in range(len(dicGraph)-1):   
        check = 0           
        for i in range(len(w)):     
            if dis[v1[i]] + w[i] < dis[v2[i]]:
                dis[v2[i]] = dis[v1[i]] + w[i]
                check = 1
        if check == 0: break

    return dis
    
#################################################################
def LabelSetting_Dic(G,source,INF=float("inf")):
    dicGraph = G
    nodes = len(dicGraph.keys())
    dis = dict((k,INF) for k in range(nodes))
    dis[source] = 0
    visitSet = set()
    visitSet.add(source)
    
    for i in range(nodes):
        a = -1 
        b = -1
        min = INF
        
        for vertex in dicGraph.keys():
            if vertex in visitSet:
                for neibor in dicGraph[vertex]:
                    if neibor not in visitSet and dis[vertex]+dicGraph[vertex][neibor]<min:
                        a = vertex
                        b = neibor
                        min = dis[vertex]+dicGraph[vertex][neibor]
        # Travel all the edges 
        if a == -1 or b == -1: break
        
        # Store weight from a to b
        dis[b] = min
        visitSet.add(b)   
    
    
    newdis={}
    temp = dis.values()
    for i in range(1,len(temp)):
        newdis[i]=temp[i]
    return newdis    
    
#################################################################
def Dijkstra_matix(G,INF=float("inf")):
    
    starter = 0
    matrix = G
    nodes = len(matrix)
    dis = dict((k,INF) for k in range(nodes))
    visit = dict((k,False) for k in range(nodes)) 
    dis[starter] = 0
     
    for i in range(nodes):
        a = -1
        min = INF
        for j in range(nodes):
            if (not (visit[j]) and dis[j]<min):
                a = j
                min = dis[j]
                
        if (a == -1):break
        visit[a] = True
         
        for b in range(nodes):
            if (not(visit[b]) and dis[a]+matrix[a][b]<dis[b]):
                dis[b] = dis[a]+matrix[a][b]
                
    return dis            
    
#################################################################    
def BellmanFord_matrix(G,INF=float("inf")):
    starter = 0
    matrix = G
    nodes = len(matrix)
    dis = dict((k,INF) for k in range(nodes))
    visit = dict((k,False) for k in range(nodes)) 
    dis[starter] = 0
    
    for i in range(nodes-1):
        for a in range(nodes):
            for b in range(nodes):
                if (dis[a] != INF and matrix[a][b] != INF):
                    if ( dis[a]+ matrix[a][b] < dis[b]):
                        dis[b] = dis[a]+matrix[a][b]
    return dis     

#################################################################    
def LabelSetting_matrix(G,INF=float("inf")): 
    # init. vertices
    matrix = G 
    nodes = len(matrix)
    dis = dict((k,INF) for k in range(nodes))
    visit = dict((k,False) for k in range(nodes)) 
    
    source = 0
    dis[source]= 0
    visit[source] = True;
    
    for vertex in range(nodes):
        a = -1
        b = -1
        min = INF
        
        #Find a vertex on SPT(Shortest Path Tree)
        for i in range(nodes):
            if visit[i]:
                #Find a vertex adjacent to SPT
                for j in range(nodes):
                    # Find min weight vertex connect to SPT
                    if not visit[j] and dis[i] + matrix[i][j] < min:
                        a = i 
                        b = j
                        min = dis[i]+matrix[i][j]
        
        # Travel all the edges 
        if a == -1 or b == -1: break
        
        # Store weight from a to b
        dis[b] = min
        visit[b] = True       
       
    return dis

#################################################################
if __name__ == "__main__":
    
    bye = 1
    source = 1
    while (bye != 0):
        # Generate a weight matrix
        numNode = raw_input("How many nodes you want to test?")
        
        # Initialize the required parameters
        G_startTime = time.time()
        Graph = iniVal(int(numNode))
        print ("----- Initializing needs ",(time.time() - G_startTime)," sec")
        print ("-----------------------------------------------------")
         
        # Dijkstra with matrix structure
        Dij_matrix_starttime = time.time()
        Dij_matrix_dis = Dijkstra_matix(Graph[0])
#         print (Dij_matrix_dis.values())
        print ( "\n=Dijkstra(matrix)=" ) 
        print ("----- Time cost : ",(time.time() - Dij_matrix_starttime)," sec")
        print ("*********************************************")
          
        # Dijkstra with dictionary structure
        Dij_dic_starttime = time.time()
        Dij_dic_dis = Dijkstra_Dic(Graph[1],source)
#         print (Dij_dic_dis.values())
        print ( "\n=Dijkstra(dictionary)=")
        print ("----- Time cost : ",(time.time() - Dij_dic_starttime)," sec")
        print ("*********************************************")   
          
        # Bellman-Ford with matrix structure
        BF_matrix_starttime = time.time()
        BF_matrix_dis = BellmanFord_matrix(Graph[0])
#         print (BF_matrix_dis.values())
        print ( "\n=Bellman-Ford(matrix)=")
        print ("----- Time cost : ",(time.time() - BF_matrix_starttime)," sec")
        print ("*********************************************")
         
        # Bellman-Ford with dictionary structure
        BF_dic_starttime = time.time()
        BF_dic_dis = BellmanFord_Dic(Graph[1], source)
#         print (BF_dic_dis.values())
        print ( "\n=Bellman-Ford(dictionary)=")
        print ("----- Time cost : ",(time.time() - BF_dic_starttime)," sec")
        print ("*********************************************")
         
        # Label Setting with matrix structure
        LS_matrix_starttime = time.time()
        LS_matrix_dis = LabelSetting_matrix(Graph[0])
#         print (LS_matrix_dis.values())
        print ( "\n=Label Setting(matrix)=")
        print ("----- Time cost : ",(time.time() - LS_matrix_starttime)," sec")
        print ("*********************************************")
            
        # Label Setting with dictionary structure
        LS_dic_starttime = time.time()
        LS_dic_dis = LabelSetting_Dic(Graph[1],source)
#         print (LS_dic_dis.values())
        print ( "\n=Label Setting(matrix)=")
        print ("----- Time cost : ",(time.time() - LS_dic_starttime)," sec")
        print ("*********************************************")
         
        print ("-----------------------------------------------------")
        # Ask if exit the program
        bye = int(raw_input("\ncontinue? (1=yes,0=no):"))
        while (bye != 0 and bye != 1):
            print ("*** Wrong input ***")
            bye = int(raw_input("\ncontinue? (1=yes,0=no):"))
             
        if bye == 0:
            print ("Bye bye !!")