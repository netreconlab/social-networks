import matplotlib.pyplot as plt
import networkx as nx
import scipy
import pandas as pd
import csv
import sys
import random

    
def main():
    G =nx.Graph()
    with open('edges.csv') as gl:
        reader = csv.reader(gl, delimiter = ',')
           
        for row in reader:
            G.add_edge(row[0], row[1], weight= float(row[2]))
    
    print('graph built')
    clust= nx.k_core(G, k=3).edges()
    G.clear()
    G.add_edges_from(clust)
    
    
    print(nx.info(G))
    nx.draw(G)
    plt.show()

main()