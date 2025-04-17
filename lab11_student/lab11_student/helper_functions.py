import csv

###########################################################################################
############################# PASTE YOUR LAB10 FUNCTIONS HERE #############################

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
    return list(p)


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



##############################################################################################
############################# COMPLETE YOUR LAB11 FUNCTIONS HERE #############################


def in_out_degree(G):
    """In and out degree of a directed graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary

    Returns
    -------
        A dictionary containing the in and out degree of each node
    """

    # WRITE YOUR CODE HERE
    R = {}
    for i in G:
        out_deg = len(G[i])
        count = 0
        for j in G:
            for k in G[j]:
                # nei, wei = k
                if k[0] == i:
                    count+=1
        R[i] = (count,out_deg)

    return R



def degree(G):
    """Degree of a directed graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary

    Returns
    -------
        A dictionary containing the degree of each node
    """

    # WRITE YOUR CODE HERE
    R = {}
    for i in G:
        R[i] = len(G[i])

    return R


def getInNeighbors(G, node):
    """In neighbors of a node in a directed graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary
    node :
        The node whose in neighbors

    Returns
    -------
        A list of in neighbors of the node
    """

    # WRITE YOUR CODE HERE
    P = []
    for i in G:
        for j in G[i]:
            if j[0] == node:
                P.append(i)

    return P


def getOutNeighbors(G, node):
    """Out neighbors of a node in a directed graph

    Parameters
    ----------
    G :
        A graph represented as a dictionary
    node :
        The node whose out neighbors

    Returns
    -------
        A list of out neighbors of the node
    """

    # WRITE YOUR CODE HERE
    P = []
    for i in G[node]:
        P.append(i[0])
    
    return P


def isNeighbor(G, node1, node2):
    """Returns True if Node2 is a neighbor of Node1 in a directed graph G.

    Parameters
    ----------
    G : dict
        A directed graph as an adjacency list.
    Node1 : any
        The node to check outgoing edges from.
    Node2 : any
        The node to check as a neighbor of Node1.

    Returns
    -------
    bool
        True if there is an edge from Node1 to Node2, False otherwise.
    """

    # WRITE YOUR CODE HERE
    falg = False
    for i in G[node1]:
        if i[0] == node2:
            falg = True
    
    return falg


def initialize_matrix(rows, cols):
    """Initialize a matrix with -1

    Parameters
    ----------
    rows : int
        number of rows
    cols : int
        number of columns

    Returns
    -------
    list[list[int]]
        A matrix with -1
    """
    # WRITE YOUR CODE HERE
    return ([[-1 for i in range(cols)] for j in range(rows)])


def adjlst_to_adj_matrix(G):
    """Convert adjacency list to adjacency matrix

    Parameters
    ----------
    G :
        A graph represented as a dictionary

    Returns
    -------
        An adjacency matrix of the graph
    """

    # WRITE YOUR CODE HERE
    P = listOfNodes(G)
    R = initialize_matrix(len(P),len(P))
    for i in G:
        for j in G[i]:
            q = P.index(i)
            w = P.index(j[0])
            R[q][w] = j[1]
            
    return R




def csv_to_adj_list(filename: str):
    """Convert CSV to adjacency list

    Parameters
    ----------
    filename : str
        The name of the CSV file

    Returns
    -------
        A graph represented as a dictionary
    """

    # WRITE YOUR CODE HERE
    G = {}
    rows = []
    with open(filename, 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            rows.append(row)
    # print(header)
    # print(rows)
    list_ofNodes = header[1:len(header)]
    addNodes(G,list_ofNodes)
    for i in rows:
        node = i[0]
        neigh = i[1:]
        for j in range(len(neigh)):
            if neigh[j] != "-1" and neigh[j] != "0":
                G[node].append((list_ofNodes[j], int(neigh[j])))

    # print(G)
    return G

                


    
            





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
# pytest tests/test_helper_functions.py