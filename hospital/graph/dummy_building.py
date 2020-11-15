# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 21:44:44 2020

@author: Paula
"""

import networkx as nx
import matplotlib.pyplot as plt
#import osmnx as ox
from math import *

def getDummyBuild():
    #------------------------------------------------------------------------------
    #Initialize the network x graph for the dummy building
    #------------------------------------------------------------------------------
    
    G = nx.Graph()
    
    #Level1------------------------------------------------------------------------
    nodes0= [(10001, {'building':1,'level':0,'room':1,'function':'door','coordinates':[6,0.5,0]}),
            (10002, {'building':1,'level':0,'room':2,'function':'information','coordinates':[7,1,0]}),
            (10003, {'building':1,'level':0,'room':3,'function':'medical','coordinates':[8,2,0]}),
            (10004, {'building':1,'level':0,'room':4,'function':'medical','coordinates':[9,2,0]}),
            (10005, {'building':1,'level':0,'room':5,'function':'medical','coordinates':[10,2,0]}),
            (10006, {'building':1,'level':0,'room':6,'function':'medical','coordinates':[11,2,0]}),
            (10007, {'building':1,'level':0,'room':7,'function':'door','coordinates':[11.5,3,0]}),
            (10008, {'building':1,'level':0,'room':8,'function':'medical','coordinates':[11,4,0]}),
            (10009, {'building':1,'level':0,'room':9,'function':'medical','coordinates':[10.25,4,0]}),
            (10010, {'building':1,'level':0,'room':10,'function':'medical','coordinates':[9.5,4,0]}),
            (10011, {'building':1,'level':0,'room':11,'function':'medical','coordinates':[8.75,4,0]}),
            (10012, {'building':1,'level':0,'room':12,'function':'medical','coordinates':[8,4,0]}),
            (10013, {'building':1,'level':0,'room':13,'function':'medical','coordinates':[7,5,0]}),
            (10014, {'building':1,'level':0,'room':14,'function':'medical','coordinates':[7,6,0]}),
            (10015, {'building':1,'level':0,'room':15,'function':'medical','coordinates':[7,7,0]}),
            (10016, {'building':1,'level':0,'room':16,'function':'medical','coordinates':[7,8,0]}),
            (10017, {'building':1,'level':0,'room':17,'function':'door','coordinates':[6,8.5,0]}),
            (10018, {'building':1,'level':0,'room':18,'function':'stairs','coordinates':[5,8,0]}),
            (10019, {'building':1,'level':0,'room':19,'function':'lift','coordinates':[5,7,0]}),
            (10020, {'building':1,'level':0,'room':20,'function':'emergency','coordinates':[5,6,0]}),
            (10021, {'building':1,'level':0,'room':21,'function':'toilet','coordinates':[4,4,0]}),
            (10022, {'building':1,'level':0,'room':22,'function':'medical','coordinates':[3,4,0]}),
            (10023, {'building':1,'level':0,'room':23,'function':'medical','coordinates':[2,4,0]}),
            (10024, {'building':1,'level':0,'room':24,'function':'medical','coordinates':[1.5,4,0]}),
            (10025, {'building':1,'level':0,'room':25,'function':'medical','coordinates':[1,3,0]}),
            (10026, {'building':1,'level':0,'room':26,'function':'medical','coordinates':[1,2.5,0]}),
            (10027, {'building':1,'level':0,'room':27,'function':'medical','coordinates':[2,2,0]}),
            (10028, {'building':1,'level':0,'room':28,'function':'medical','coordinates':[3,2,0]}),
            (10029, {'building':1,'level':0,'room':29,'function':'lift','coordinates':[4,2,0]}),
            (10030, {'building':1,'level':0,'room':30,'function':'stairs','coordinates':[5,1,0]}),
            (10031, {'building':1,'level':0,'room':31,'function':'floor','coordinates':[6,3,0]}),
            (10032, {'building':1,'level':0,'room':32,'function':'floor','coordinates':[8,3,0]}),
            (10033, {'building':1,'level':0,'room':33,'function':'floor','coordinates':[10,3,0]}),
            (10034, {'building':1,'level':0,'room':34,'function':'floor','coordinates':[6,5.5,0]}),
            (10035, {'building':1,'level':0,'room':35,'function':'floor','coordinates':[6,7,0]}),
            (10036, {'building':1,'level':0,'room':36,'function':'floor','coordinates':[4,3,0]}),
            (10037, {'building':1,'level':0,'room':37,'function':'floor','coordinates':[2,3,0]})]
    
    edges0 = [(10001,10002,1),(10001,10031,1),(10002,10031,1),(10031,10032,1),
              (10031,10034,1),(10031,10030,1),(10031,10029,1),(10031,10036,1),
              (10031,10021,1),(10032,10003,1),(10032,10003,1),(10032,10004,1),
              (10032,10005,1),(10032,10012,1),(10032,10011,1),(10032,10010,1),
              (10032,10033,1),(10033,10006,1),(10033,10007,1),(10033,10008,1),
              (10033,10009,1),(10034,10013,1),(10034,10014,1),(10034,10020,1),
              (10034,10035,1),(10035,10015,1),(10035,10016,1),(10035,10017,1),
              (10035,10019,1),(10018,10035,1),(10018,10017,1),(10017,10016,1),
              (10017,10019,1),(10036,10022,1),(10036,10023,1),(10036,10028,1),
              (10036,10037,1),(10037,10024,1),(10036,10025,1),(10036,10026,1),
              (10036,10027,1)]
    
    nodes1= [(10101, {'building':1,'level':1,'room':1,'function':'cleaning','coordinates':[7,1,2.5]}),
            (10102, {'building':1,'level':1,'room':2,'function':'medical','coordinates':[8,2,2.5]}),
            (10103, {'building':1,'level':1,'room':3,'function':'medical','coordinates':[9,2,2.5]}),
            (10104, {'building':1,'level':1,'room':4,'function':'medical','coordinates':[10,2,2.5]}),
            (10105, {'building':1,'level':1,'room':5,'function':'medical','coordinates':[11,2,2.5]}),
            (10106, {'building':1,'level':1,'room':6,'function':'door','coordinates':[11.5,3,2.5]}),
            (10107, {'building':1,'level':1,'room':7,'function':'toilet','coordinates':[11,4,2.5]}),
            (10108, {'building':1,'level':1,'room':8,'function':'medical','coordinates':[10,4,2.5]}),
            (10109, {'building':1,'level':1,'room':9,'function':'medical','coordinates':[9,4,2.5]}),
            (10110, {'building':1,'level':1,'room':10,'function':'medical','coordinates':[8,4,2.5]}),
            (10111, {'building':1,'level':1,'room':11,'function':'medical','coordinates':[7,5,2.5]}),
            (10112, {'building':1,'level':1,'room':12,'function':'medical','coordinates':[7,6,2.5]}),
            (10113, {'building':1,'level':1,'room':13,'function':'medical','coordinates':[7,7.5,2.5]}),
            (10114, {'building':1,'level':1,'room':14,'function':'stairs','coordinates':[5.5,8,2.5]}),
            (10115, {'building':1,'level':1,'room':15,'function':'lift','coordinates':[5,7,2.5]}),
            (10116, {'building':1,'level':1,'room':16,'function':'staff','coordinates':[4,7,2.5]}),
            (10117, {'building':1,'level':1,'room':17,'function':'medical','coordinates':[3,6,2.5]}),
            (10118, {'building':1,'level':1,'room':18,'function':'toilet','coordinates':[4,5,2.5]}),
            (10119, {'building':1,'level':1,'room':19,'function':'medical','coordinates':[2,4,2.5]}),
            (10120, {'building':1,'level':1,'room':20,'function':'medical','coordinates':[1,3.5,2.5]}),
            (10121, {'building':1,'level':1,'room':21,'function':'medical','coordinates':[1,2.5,2.5]}),
            (10122, {'building':1,'level':1,'room':22,'function':'medical','coordinates':[2,2,2.5]}),
            (10123, {'building':1,'level':1,'room':23,'function':'medical','coordinates':[3,2,2.5]}),
            (10124, {'building':1,'level':1,'room':24,'function':'lift','coordinates':[4,2,2.5]}),
            (10125, {'building':1,'level':1,'room':25,'function':'stairs','coordinates':[5.5,1,2.5]}),
            (10126, {'building':1,'level':1,'room':26,'function':'floor','coordinates':[6,3,2.5]}),
            (10127, {'building':1,'level':1,'room':27,'function':'floor','coordinates':[8,3,2.5]}),
            (10128, {'building':1,'level':1,'room':28,'function':'floor','coordinates':[10,3,2.5]}),
            (10129, {'building':1,'level':1,'room':29,'function':'floor','coordinates':[5,5,2.5]}),
            (10130, {'building':1,'level':1,'room':30,'function':'floor','coordinates':[6,7,2.5]}),
            (10131, {'building':1,'level':1,'room':31,'function':'floor','coordinates':[3,3,2.5]})]
    
    edges1 = [(10126,10101,1),(10126,10125,1),(10126,10127,1),(10126,10129,1),
              (10126,10124,1),(10126,10131,1),(10127,10102,1),(10127,10103,1),
              (10127,10128,1),(10127,10109,1),(10127,10110,1),(10128,10104,1),
              (10128,10105,1),(10128,10106,1),(10128,10107,1),(10128,10108,1),
              (10129,10111,1),(10129,10112,1),(10129,10117,1),(10129,10116,1),
              (10129,10118,1),(10130,10113,1),(10130,10114,1),(10130,10115,1),
              (10130,10129,1),(10131,10119,1),(10131,10120,1),(10131,10121,1),
              (10131,10122,1),(10131,10123,1),(10131,10124,1)]
    
    nodes2= [(10201, {'building':1,'level':2,'room':1,'function':'cleaning','coordinates':[7,1,5]}),
            (10202, {'building':1,'level':2,'room':2,'function':'clinical','coordinates':[7.75,2,5]}),
            (10203, {'building':1,'level':2,'room':3,'function':'clinical','coordinates':[8.75,2,5]}),
            (10204, {'building':1,'level':2,'room':4,'function':'clinical','coordinates':[9.25,2,5]}),
            (10205, {'building':1,'level':2,'room':5,'function':'clinical','coordinates':[10,2,5]}),
            (10206, {'building':1,'level':2,'room':6,'function':'clinical','coordinates':[11,2,5]}),
            (10207, {'building':1,'level':2,'room':7,'function':'door','coordinates':[11.5,3,5]}),
            (10208, {'building':1,'level':2,'room':8,'function':'clinical','coordinates':[11,4,5]}),
            (10209, {'building':1,'level':2,'room':9,'function':'clinical','coordinates':[10,4,5]}),
            (10210, {'building':1,'level':2,'room':10,'function':'clinical','coordinates':[9.25,4,5]}),
            (10211, {'building':1,'level':2,'room':11,'function':'clinical','coordinates':[8.75,4,5]}),
            (10212, {'building':1,'level':2,'room':12,'function':'clinical','coordinates':[7.75,4,5]}),
            (10213, {'building':1,'level':2,'room':13,'function':'clinical','coordinates':[7,5,5]}),
            (10214, {'building':1,'level':2,'room':14,'function':'clinical','coordinates':[7,6,5]}),
            (10215, {'building':1,'level':2,'room':15,'function':'clinical','coordinates':[7,6.75,5]}),
            (10216, {'building':1,'level':2,'room':16,'function':'clinical','coordinates':[7,7.5,5]}),
            (10217, {'building':1,'level':2,'room':17,'function':'stairs','coordinates':[5.5,8,5]}),
            (10218, {'building':1,'level':2,'room':18,'function':'lift','coordinates':[5,7,5]}),
            (10219, {'building':1,'level':2,'room':19,'function':'cafeteria','coordinates':[4,6.5,5]}),
            (10220, {'building':1,'level':2,'room':20,'function':'roofdeck','coordinates':[4,5.5,5]}),
            (10221, {'building':1,'level':2,'room':21,'function':'visitors','coordinates':[4,4,5]}),
            (10222, {'building':1,'level':2,'room':22,'function':'toilet','coordinates':[2,4,5]}),
            (10223, {'building':1,'level':2,'room':23,'function':'clinical','coordinates':[1.25,3,5]}),
            (10224, {'building':1,'level':2,'room':24,'function':'clinical','coordinates':[1.5,2,5]}),
            (10225, {'building':1,'level':2,'room':25,'function':'clinical','coordinates':[2.5,2,5]}),
            (10226, {'building':1,'level':2,'room':26,'function':'clinical','coordinates':[3.25,2,5]}),
            (10227, {'building':1,'level':2,'room':27,'function':'lift','coordinates':[4,2,5]}),
            (10228, {'building':1,'level':2,'room':28,'function':'stairs','coordinates':[5.5,1,5]}),
            (10229, {'building':1,'level':2,'room':29,'function':'floor','coordinates':[6,3,5]}),
            (10230, {'building':1,'level':2,'room':30,'function':'floor','coordinates':[8,3,5]}),
            (10231, {'building':1,'level':2,'room':31,'function':'floor','coordinates':[10,3,5]}),
            (10232, {'building':1,'level':2,'room':32,'function':'floor','coordinates':[5.5,5,5]}),
            (10233, {'building':1,'level':2,'room':33,'function':'floor','coordinates':[6,6.5,5]}),
            (10234, {'building':1,'level':2,'room':34,'function':'floor','coordinates':[3,3,5]})]
    
    edges2 = [(10228,10229,1),(10229,10201,1),(10229,10230,1),(10229,10232,1),
              (10229,10221,1),(10229,10234,1),(10229,10227,1),(10234,10226,1),
              (10234,10227,1),(10234,10225,1),(10234,10224,1),(10234,10223,1),
              (10234,10222,1),(10232,10220,1),(10232,10219,1),(10232,10218,1),
              (10232,10233,1),(10232,10214,1),(10232,10213,1),(10233,10216,1),
              (10233,10217,1),(10233,10218,1),(10233,10215,1),(10230,10202,1),
              (10230,10203,1),(10230,10204,1),(10230,10231,1),(10230,10210,1),
              (10230,10211,1),(10230,10212,1),(10231,10209,1),(10231,10208,1),
              (10231,10207,1),(10231,10205,1),(10231,10206,1)]
    
    edgesbetweenlevels = [(10030,10125,2.5),(10125,10228,2.5),(10029,10124,2.5),
                          (10124,10227,2.5),(10018,10114,2.5),(10114,10217,2.5),
                          (10019,10115,2.5),(10115,10218,2.5)]
    #------------------------------------------------------------------------------
    #Add nodes and edges from both lists to the graph
    #------------------------------------------------------------------------------
    G.add_nodes_from(nodes0)
    G.add_weighted_edges_from(edges0)
    
    G.add_nodes_from(nodes1)
    G.add_weighted_edges_from(edges1)
    
    G.add_nodes_from(nodes2)
    G.add_weighted_edges_from(edges2)
    
    G.add_weighted_edges_from(edgesbetweenlevels)
    
    #------------------------------------------------------------------------------
    #Update edge weights
    #------------------------------------------------------------------------------
    nodes_pos_dict = dict()
    color_map = []
    for n in G.nodes():
        item = {n:(G.nodes[n]['coordinates'][0],G.nodes[n]['coordinates'][1])}
        nodes_pos_dict.update(item)
        if G.nodes[n]['function'] == 'door' or G.nodes[n]['function'] == 'stairs':
            color_map.append('green')
        else:
            color_map.append('black')
        
        
    for e in G.edges():
        if G.nodes[e[0]]['coordinates'][2] != G.nodes[e[1]]['coordinates'][2]:
            ce0 = G.nodes[e[0]]['coordinates']
            ce1 = G.nodes[e[1]]['coordinates']
            d = sqrt(abs(ce0[0]-ce1[0]))*abs(abs(ce0[0]-ce1[0])) + abs(ce0[1]-ce1[1])*abs(ce0[1]-ce1[1])
            G[e[0]][e[1]]['weight']=d
    
   
    return(G,nodes_pos_dict)
    
    



