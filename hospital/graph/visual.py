# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 14:16:59 2020

@author: Paula
"""

import networkx as nx
import matplotlib.pyplot as plt
import osmnx as ox
from math import *
import Hackathon_dummyBuilding as dm
import imageio
import os

def getLevel(G,node):
    nodes = []
    for n in G.nodes():
        if G.nodes[node]['coordinates'][2] == G.nodes[n]['coordinates'][2]:
            nodes.append(n)
    return(G.subgraph(nodes),G.nodes[node]['level'])


def path(ziel):   
    aim_list = {'Kardiologie':10123,'Onkologie':10111,'Allgemeinmedizin':10010,'HNO':10104,
           'Gynaokologie':10022,'Urologie':10027,'Besuchraum09':10209}
    aim = aim_list[ziel]
    
    G,pos = dm.getDummyBuild()
    shortest_path = nx.shortest_path(G,10001,aim)
    filenames = []
    print(shortest_path)
        
    i = 0
    for node in shortest_path:
        x_blue = []
        y_blue = []
        x_cyan = []
        y_cyan = []
        x_green = []
        y_green = []
        H,level = getLevel(G,node)
        for j in range(len(shortest_path)):
            if G.nodes[shortest_path[j]]['level']==level:
                if shortest_path[j]==node:
                    x_cyan.append(H.nodes[shortest_path[j]]['coordinates'][0])
                    y_cyan.append(H.nodes[shortest_path[j]]['coordinates'][1])
                    if j< len(shortest_path)-1 and G.nodes[shortest_path[j+1]]['level']==level:
                        x_cyan.append(H.nodes[shortest_path[j+1]]['coordinates'][0])
                        y_cyan.append(H.nodes[shortest_path[j+1]]['coordinates'][1])
                if H.nodes[shortest_path[j]]['level']==level:
                    x_blue.append(H.nodes[shortest_path[j]]['coordinates'][0])
                    y_blue.append(H.nodes[shortest_path[j]]['coordinates'][1])
        #color important nodes
        for n in H.nodes():
            x1 = H.nodes[n]['coordinates'][0]
            y1 = H.nodes[n]['coordinates'][1]
            if H.nodes[n]['function'] == 'door' or H.nodes[n]['function'] == 'stairs':
                x_green.append(x1)
                y_green.append(y1)
        fig = plt.figure(i)
        if level == 0:
            img = plt.imread('EG.png')
        elif level == 1:
            img = plt.imread('1OG.png')
        else:
            img = plt.imread('2OG.png')
        #plt.scatter(x,y,zorder=1)
        plt.plot(x_blue,y_blue,'b-o')
        plt.plot(x_green,y_green,'go')
        plt.plot(x_cyan,y_cyan,'c-o')
        plt.axis('off')
        plt.imshow(img, extent=[0.0, 12.0, -0.5, 10.0])
        
        fig.savefig(str(i)+'building.png', dpi=200)
        filenames.append(str(i)+'building.png')
        
        i+=1
        
    
    print(filenames)
    
    images = []
    for filename in filenames:
        images.append(imageio.imread(filename))
        os.remove(filename)
    imageio.mimsave('movie.gif', images, duration=5)



path('Besuchraum09')







