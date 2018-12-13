import matplotlib.pyplot as plt
import networkx as nx
import scipy
import pandas as pd
import csv
import sys

def edge_to_remove(G):
    #creates a dictionary of betweeness values for each edge
    dict_1= nx.edge_betweenness_centrality(G)
    #turns the dictionary into a list
    tuple_list= dict_1.items()
    #sorts list of tuples based on betweeness values in ascending order
    sorted(tuple_list, key = lambda x:x[1], reverse= True)
    #returns edge as (a,b)
    return tuple_list

def btw_centrality(G, k):
    c= edge_to_remove(G)
    list_c =[*c]
    i = 0
    for i in range(len(list_c)-1):
        if list_c[i][1]< k:
            G.remove_edge(*list_c[i][0])
            print('Edges removed = ', list_c[i][0])
        i+=1
    
    


def main():
    G =nx.Graph()
    with open('1-edges.csv') as gl:
        reader = csv.reader(gl, delimiter = ',')
           
        for row in reader:
            G.add_edge(row[0], row[1], weight= float(row[2]))

    H =nx.Graph()
    with open('2-edges.csv') as gl:
        reader = csv.reader(gl, delimiter = ',')
           
        for row in reader:
            H.add_edge(row[0], row[1], weight= float(row[2]))
    #H_btw= nx.betweenness_centrality(H, k=20, weight=None, endpoints= False, seed= None)
    #print("the first element is " + str(H_btw[1]))
    G.add_edges_from(H.edges())
    print('graph built')
    
    btw_centrality(G, .001)
    print()
    print(nx.info(G))
    nx.draw(G)
    plt.show()

main()
