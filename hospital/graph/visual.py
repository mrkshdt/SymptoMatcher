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

def getLevel(G,node):
    nodes = []
    for n in G.nodes():
        if G.nodes[node]['coordinates'][2] == G.nodes[n]['coordinates'][2]:
            nodes.append(n)
    return(G.subgraph(nodes),G.nodes[node]['level'])

G,pos = dm.getDummyBuild()
#shortest_path = nx.shortest_path(G,10001,10205)
shortest_path = nx.shortest_path(G,10001,10018)
filenames = []
print(shortest_path)
i = 0
for node in shortest_path:
    x_blue = []
    y_blue = []
    x_cyan = []
    y_cyan = []
    x_grey = []
    y_grey = []
    x_green = []
    y_green = []
    H,level = getLevel(G,node)
    #color the edges
    for e in H.edges():
        #get node coordinates
        x1 = H.nodes[e[0]]['coordinates'][0]
        y1 = H.nodes[e[0]]['coordinates'][1]
        x2 = H.nodes[e[1]]['coordinates'][0]
        y2 = H.nodes[e[1]]['coordinates'][1]
        if e[0] == node and e[1] in shortest_path:
            x_cyan.append(x1)
            y_cyan.append(y1)
            x_cyan.append(x2)
            y_cyan.append(y2)
        elif e[0] in shortest_path and e[1] in shortest_path:
            x_blue.append(x1)
            y_blue.append(y1)
            x_blue.append(x2)
            y_blue.append(y2)
        else:
            x_grey.append(x1)
            y_grey.append(y1)
            x_grey.append(x2)
            y_grey.append(y2)
    #color important nodes
    for n in H.nodes():
        x1 = H.nodes[n]['coordinates'][0]
        y1 = H.nodes[n]['coordinates'][1]
        if H.nodes[n]['function'] == 'door' or H.nodes[n]['function'] == 'stairs':
            x_green.append(x1)
            y_green.append(y1)
    # for n in H.nodes():
    #     x1 = H.nodes[n]['coordinates'][0]
    #     y1 = H.nodes[n]['coordinates'][1]
    #     if n == node:
    #         x_cyan.append(x1)
    #         y_cyan.append(y1)
    #     elif H.nodes[n]['function'] == 'door' or H.nodes[n]['function'] == 'stairs':
    #         x_green.append(x1)
    #         y_green.append(y1)
    #     elif n in shortest_path:
    #         x_blue.append(x1)
    #         y_blue.append(y1)
    #     else:
    #         x_grey.append(x1)
    #         y_grey.append(y1)
    fig = plt.figure(i)
    if level == 0:
        img = plt.imread('EG.png')
    elif level == 1:
        img = plt.imread('EG.png')
    else:
        img = plt.imread('EG.png')
    #plt.scatter(x,y,zorder=1)
    plt.plot(x_green,y_green,'go')
    plt.plot(x_cyan,y_cyan,'c-o')
    plt.plot(x_blue,y_blue,'b-o')
    plt.plot(x_grey,y_grey,'ko')
    plt.axis('off')
    plt.imshow(img, extent=[0.0, 12.0, -0.5, 10.0])
    
    fig.savefig(str(i)+'building.png')
    filenames.append(str(i)+'building.png')
    
    i+=1
    

print(filenames)

images = []
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('movie.gif', images, duration=5)

#plt.show() 



#imgplot.save('out.gif', save_all=True, append_images=[im1, im2, ...])









