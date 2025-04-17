from helper_functions import *


def create_airport_graph():
    """Create an adjacency list representation of the airport graph.

    Returns
    -------
        The adjacency list representation of the airport graph
    """

    # WRITE YOUR CODE HERE
    G = {}
    Nodes = ["Austin","Atlanta","Chicago","Dallas", "Denver","Houston", "Washington"]
    addNodes(G, Nodes)
    Edges = [("Austin", "Dallas", 200),("Austin", "Houston", 160),("Austin", "Dallas", 200),("Dallas","Austin",200),
             ("Dallas","Denver",780),("Dallas","Chicago",900), ("Chicago","Denver",1000), ("Denver","Chicago",1000),
             ("Denver","Atlanta",1400),("Atlanta","Washington",600),("Atlanta","Houston",800), ("Houston","Atlanta",800),
             ("Washington","Atlanta",600),("Washington","Dallas",1300)]
    addEdges(G,Edges,directed=True)
    return G

def one_way_connection(G):
    """Obtain the list of one-way connections in the graph.

    Parameters
    ----------
    G :
        The adjacency list representation of the graph.

    Returns
    -------
        The list of one-way connections in the graph.
    """

    # WRITE YOUR CODE HERE
    d = []
    for i in G:
        for j in G[i]:
            q = []
            for l in G[j[0]]:
                q.append(l[0])
            if i not in q:
                d.append((i,j[0]))

    return d


             



def nearest_airport(G, A):
    """Find the nearest airport to a given airport.

    Parameters
    ----------
    G :
        The adjacency list representation of the graph.
    A :
        The airport for which the nearest airport is to be found.

    Returns
    -------
        The nearest airport to the given airport.
    """

    # WRITE YOUR CODE HERE
    return (getNearestNeighbor(G, A))


def not_more_than_one_intermediate(G, node):
    """Find the airports connected to a given airport with not more than one
    intermediate airport.

    Parameters
    ----------
    G :
        The adjacency list representation of the graph.
    node :
        The airport for which the connected airports are to be found.

    Returns
    -------
        The airports connected to the given airport with not more than one intermediate
        airport.
    """

    # WRITE YOUR CODE HERE
    e = []
    for k,v in G.items():
        q = []
        for l in v:
            q.append(l[0])
        if node in q:
            e.append(k)
        else:
            w = []
            for i in q:
                for j in G[i]:
                    w.append(j[0])
            if node in w:
                e.append(k)
                
    if node in e:
        e.remove(node)
    
    return e


def alien_attack(G):
    """Aliens have attacked, remove Washington, add a path from Atlanta to Dallas and
    return the updated graph.

    Parameters
    ----------
    G :
        The adjacency list representation of the graph.

    Returns
    -------
        The updated adjacency list representation of the graph.
    """

    # WRITE YOUR CODE HERE
    removeNode(G, node="Washington")
    Edges = [("Atlanta","Dallas",1700)]
    addEdges(G, Edges)
    return G


#############################################################################
# Let's test your code... Run your code file and check manually whether the #
# code is running as expected...                                            #
#############################################################################
if __name__ == "__main__":
    print("GRAPH")
    G = create_airport_graph()
    displayGraph(G)
    '''
    SHOULD PRINT:
    {'Dallas': [('Austin', 200), ('Denver', 780), ('Chicago', 900)], 'Austin': [('Dallas', 200), ('Houston', 160)], 
    'Washington': [('Dallas', 1300), ('Atlanta', 600)], 'Denver': [('Atlanta', 1400), ('Chicago', 1000)], 
    'Atlanta': [('Washington', 600), ('Houston', 800)], 'Chicago': [('Denver', 1000)], 'Houston': [('Atlanta', 800)]}
    '''

    print()
    print("ONE WAY CONNECTION")
    print(one_way_connection(G))
    '''
    SHOULD PRINT:
    [('Dallas', 'Denver'), ('Dallas', 'Chicago'), ('Austin', 'Houston'), ('Washington', 'Dallas'), ('Denver', 'Atlanta')]
    '''

    print()
    print("NEAREST AIRPORT")
    for i in listOfNodes(G):
        print(i,":", nearest_airport(G, i))
    '''
    SHOULD PRINT:
    Dallas : Austin
    Austin : Houston
    Washington : Atlanta
    Denver : Chicago
    Atlanta : Washington
    Chicago : Denver
    Houston : Atlanta
    '''

    print()
    print("CONNECTED WITH NOT MORE THAN ONE INTERMEDIATE AIRPORT")
    print("Dallas :", not_more_than_one_intermediate(G, "Dallas"))
    '''
    SHOULD PRINT:
    Dallas : ['Austin', 'Washington', 'Atlanta']
    '''

    print()
    print("REMOVING WASHINGTON, ADDING PATH FROM ATLANTA TO DALLAS AND DISPLAYING A GRAPH")
    removeNode(G, "Washington")
    addEdges(G,[("Atlanta","Dallas",1700)])
    displayGraph(G)
    '''
    SHOULD PRINT:
    {
        'Dallas': [('Austin', 200), ('Denver', 780), ('Chicago', 900), ('Atlanta', 1700)], 
        'Austin': [('Dallas', 200), ('Houston', 160)], 
        'Denver': [('Atlanta', 1400), ('Chicago', 1000)], 
        'Atlanta': [('Houston', 800), ('Dallas', 1700)], 
        'Chicago': [('Denver', 1000)], 
        'Houston': [('Atlanta', 800)]
    }
    '''

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q2.py