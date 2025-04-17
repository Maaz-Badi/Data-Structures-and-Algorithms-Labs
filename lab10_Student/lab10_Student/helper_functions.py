import math

def addNodes(G, nodes) -> None:
    """Add nodes to the graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary
    nodes :
        A list of nodes to be added to the graph
    """

    # WRITE YOUR CODE HERE
    for i in nodes:
        G[i] = []


def addEdges(G, edges, directed: bool = False) -> None:
    """Add edges to the graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary
    edges :
        A list of edges to be added to the graph
    directed : bool, optional
        A boolean value to determine if the graph is directed or not, by default False
    """

    # WRITE YOUR CODE HERE
    for i in edges:
        key = i[0]
        value = (i[1],i[2])
        G[key].append(value)
        if directed == False:
            G[i[1]].append((i[0],i[2]))


def listOfNodes(G):
    """Get the list of nodes in a graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary

    Returns
    -------
        A list of nodes in the graph
    """

    # WRITE YOUR CODE HERE
    p = G.keys()
    return p


def listOfEdges(G, directed: bool = False):
    """Get the list of edges in a graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary
    directed : bool, optional
        A boolean value to determine if the graph is directed or not, by default False

    Returns
    -------
        A list of edges in the graph
    """

    # WRITE YOUR CODE HERE
    P = []
    for k,v in G.items():
        for i in v:
            o = (k,i[0],i[1])
            if directed == True:
                if o not in P:
                    P.append(o)
            else:
                y= (i[0],k,i[1])
                if (o not in P) and (y not in P):
                    P.append(o)
    
    return P



def getNeighbours(G, node):
    """Get the neighbours of a node in a graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary
    node :
        The node whose neighbours are

    Returns
    -------
        A list of neighbours of the node
    """

    # WRITE YOUR CODE HERE
    P = []
    for i in G[node]:
        P.append(i[0])
    
    return P


def getNearestNeighbor(G, node):
    """Get the nearest neighbor of a node in a graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary
    node :
        The node whose nearest neighbor

    Returns
    -------
        The nearest neighbor of the node
    """

    # WRITE YOUR CODE HERE
    max = math.inf
    index = None
    if G[node]==[]:
        return math.inf
    for i in G[node]:
        if i[1]<max:
            max = i[1]
            index = i[0]

    
    return index
        


def removeNode(G, node) -> None:
    """Remove a node from the graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary
    node :
        The node to be removed from the graph
    """

    # WRITE YOUR CODE HERE
    del(G[node])
    for k,v in G.items():
        for i in v:
            if i[0] == node:
                v.remove(i)






def removeNodes(G, nodes) -> None:
    """Remove nodes from the graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary
    nodes :
        A list of nodes to be removed from the graph
    """

    # WRITE YOUR CODE HERE
    for i in nodes:
        removeNode(G,i)


def displayGraph(G) -> None:
    """Display the graph in a human-readable format

    Parameters
    ----------
    G :
        A graph represented as a dictionary
    """

    # WRITE YOUR CODE HERE
    print (G)


#############################################################################
# Let's test your code... Run your code file and check manually whether the #
# code is running as expected...                                            #
# Visible Testcases are available in main_helper_functions.py               #
#############################################################################

if __name__ == "__main__":
    import main_helper_functions
    main_helper_functions.main()

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_helperfunctions.py