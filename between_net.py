import matplotlib.pyplot as plt
import networkx as nx
import scipy
import pandas as pd
import csv
import sys

def edge_to_remove(G):
    #creates a dictionary of betweeness values for each edge
    dict_1= nx.edge_betweenness_centrality(G, k=None, normalized=True, weight=None, seed=None)
    
    #turns the dictionary into a list
    tuple_list= dict_1.items()
    t_list= []
    for key, value in tuple_list:
        temp= [key, value]
        t_list.append(temp)
        print(temp)
    #sorts list of tuples based on betweeness values in ascending order
    sorted(t_list, key = lambda x:x[1], reverse= True)
    print('betweenness values ', t_list)
    #returns edge as (a,b)

    return t_list
def btw_centrality(G, k):
    c= edge_to_remove(G)
    list_c =[*c]
    j=1
    i = 0
    for i in range(len(list_c)-1):
        if list_c[i][j]> k:
            G.remove_edge(*list_c[i][0])
            print('c = ', list_c[i][0])
        i+=1

def main():
    G =nx.Graph()
    with open('edges.csv') as gl:
        reader = csv.reader(gl, delimiter = ',')
           
        for row in reader:
            G.add_edge(row[0], row[1], weight= float(row[2]))

    
    print("graph built")
    
    btw_centrality(G, .03)
   
    print(nx.info(G))
    
    
    nx.draw(G)
    plt.show()

main()