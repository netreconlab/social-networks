import matplotlib.pyplot as plt
import networkx as nx
import scipy
import pandas as pd
import csv
import sys
from networkx.algorithms import community

def eigenvector_removal(G, k):
    #creates a dictionary of betweeness values for each edge
    dict_1= nx.eigenvector_centrality(G, max_iter=100, tol= 1.0e-6, nstart= None, weight=None)
    #turns the dictionary into a list
     
    e_value =[]
    for key, value  in dict_1.items():
        e_value.append(key)
        e_value.append(value)

    i= 0
    j=1
    size= len(e_value)
    while i< size and j< size:
        if e_value[j]>k:
            g=G.nodes(int(e_value[i]))
            G.remove_edges_from(G, s=g,t= None, flow_func= None)
        i+=2
        j+=2

        
def main():
    G =nx.Graph()
    with open('edges.csv') as gl:
        reader = csv.reader(gl, delimiter = ',')
        weight_list= []
           
        for row in reader:
            G.add_edge(row[0], row[1], weight= float(row[2]))
            #weight_list.append(row[2])

       
        

   #[] H =nx.Graph()
    '''with open('2-edges.csv') as gl:
        reader = csv.reader(gl, delimiter = ',')
           
        for row in reader:
            H.add_edge(row[0], row[1], weight= float(row[2]))
        # h= nx.betweenness_centrality(H, k=None, normalized=True, weight=row[2], endpoints=False, seed=None)
        # print(h)
    #H_btw= nx.betweenness_centrality(H, k=20, weight=None, endpoints= False, seed= None)
    #print("the first element is " + str(H_btw[1]))
    #G.add_edges_from(H.edges())'''
    print('graph built')
    eigenvector_removal(G, 5)
    
 
    print(nx.info(G))
    nx.draw(G)
    plt.show()

main()
