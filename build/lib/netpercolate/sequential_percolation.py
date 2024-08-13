import networkx as nx
import numpy as np
import pandas as pd
from random import shuffle

# rank node by centrality measures

def rank_node(G, method = 'degree', weight = None):
    '''
    Get the node rank based on different ranking methods.

    ## Parameter
    G: Networkx graph object.
    Method: Measure used to rank the node. Default set as 'degree'.
    Weight: Edge attribute to be treated as weight to compute centrality ranks. None if the graph is unweighted. 

    ## Return
    Sorted list
    '''

    if method not in ['degree','betweenness','pagerank', 'eigen', 'closeness', 'katz', 'random']:
        raise ValueError("Measures can only be 'degree', 'betweenness', 'pagerank', 'eigen', 'closeness', 'katz', or 'random'.")

    if method == 'degree':
        _list = nx.degree_centrality(G)
    elif method == 'betweenness':
        _list = nx.betweenness_centrality(G, weight = weight)
    elif method == 'pagerank':
        _list = nx.pagerank_numpy(G, weight = None)
    elif method == 'eigen':
        _list = nx.eigenvector_centrality_numpy(G, weight = weight)
    elif method == 'closeness':
        _list = nx.closeness_centrality(G)
    elif method == 'katz':
        _list == nx.katz_centrality_numpy(G, weight = weight)
    else: # for random
        _list = list(G.nodes)
        shuffle(_list) # in place shuffle


    sorted_rank = sorted(_list, key=_list.get, reverse=True)

    return sorted_rank

# node removal algorithm
    
def standard_percolation(G, rank):
    '''
    Sequential node removal with LCC. 

    ## Parameters
    G: networkx graph object
    rank: sorted node ranking generated from `rank_node` 
    
    ## Return
    Dataframe with q fraction of nodes removed and the resulting LCC
    '''

    assert len(G) == len(rank)

    LCCs = [1] 
    q = [1]
    G_copy = G.copy()

    for node in rank:
        G_copy.remove_node(node)

        try:
            CCs = nx.connected_components(G_copy)
            LCC = len(max((component for component in CCs if len(component) > 1), key = len, default = set())) / len(G)
        except ValueError:
            LCC = 0
        
        LCCs.append(LCC)
        q.append(len(G_copy)/len(G))

    LCCs.reverse() # reverse the list to match the fraction removed
    

    LCC_df = pd.DataFrame((q, LCCs)).T.fillna(method = 'ffill')
    LCC_df = LCC_df.rename(columns={0:'Fraction',1:'LCC'})
    
    return LCC_df



