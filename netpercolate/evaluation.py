import networkx as nx
import numpy as np
import pandas as pd
from .miscel import rbo 

### Produce dissimilarity matrix between different node rankings via RBO
def RBO_matrix(ranked_list, p = 0.9):
    '''
    Produce dissimilarity matrix between different node rankings via RBO

    ## Parameters
    ranked_list: A list of ranked node list
    p: Probability of looking for overlap at rank k + 1 after having examined rank k

    ## Return
    numpy array 
    '''

    ests = []

    for i, irank in enumerate(ranked_list):
        for j, jrank in enumerate(ranked_list):
            L_estimate = rbo(irank, jrank, p=p).ext
            ests.append(L_estimate)
    
    reshaped_ests = np.array(ests).reshape(len(ranked_list), len(ranked_list))
    
    return reshaped_ests