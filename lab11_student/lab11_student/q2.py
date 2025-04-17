from helper_functions import *
import math

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
    Edges = [("Austin", "Dallas", 200),("Austin", "Houston", 160),("Dallas","Austin",200),
             ("Dallas","Denver",780),("Dallas","Chicago",900), ("Chicago","Denver",1000), ("Denver","Chicago",1000),
             ("Denver","Atlanta",1400),("Atlanta","Washington",600),("Atlanta","Houston",800), ("Houston","Atlanta",800),
             ("Washington","Atlanta",600),("Washington","Dallas",1300)]
    addEdges(G,Edges,directed=True)
    return G


def max_inbound_outbound_airport(G) -> tuple[str, str]:
    """
    Finds the airport with the highest number of inbound and outbound flights.

    Args:
        G (dict): The adjacency list representation of the graph.

    Returns:
        tuple[str, str]: A tuple containing:
            - The airport with the maximum inbound flights.
            - The airport with the maximum outbound flights.
    """

    # WRITE YOUR CODE HERE
    R = in_out_degree(G)
    maxin = 0
    maxout = 0
    maxairin = None
    maxairout = None
    for i in R:
        if R[i][0]>maxin:
            maxin = R[i][0]
            maxairin = i
        if R[i][1]>maxout:
            maxout = R[i][1]
            maxairout = i

    return (maxairin,maxairout)



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
    {
        'Dallas': [('Austin', 200), ('Denver', 780), ('Chicago', 900)], 
        'Austin': [('Dallas', 200), ('Houston', 160)], 
        'Washington': [('Dallas', 1300), ('Atlanta', 600)], 
        'Denver': [('Atlanta', 1400), ('Chicago', 1000)], 
        'Atlanta': [('Washington', 600), ('Houston', 800)], 
        'Chicago': [('Denver', 1000)], 
        'Houston': [('Atlanta', 800)]
    }
    '''

    max_inbound, max_outbound = max_inbound_outbound_airport(G)
    print("MAXIMUM IN-BOUND:", max_inbound)     #   SHOULD PRINT: Atlanta

    print("MAXIMUM OUT-BOUND:", max_outbound)   #   SHOULD PRINT: Dallas


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q2.py