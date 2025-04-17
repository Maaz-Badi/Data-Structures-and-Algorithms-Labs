import math 
from HelperFunctions import *
from q1 import *

def GetShortestPath(graph, source, destination):
    """
    Finds the shortest path from source to destination using Dijkstra's algorithm.

    Args:
        graph (dict): A dictionary of nodes and their neighbors with edge weights.
        source (any): The starting node.
        destination (any): The target node.

    Returns:
        list: A list of (prev_node, node, weight) tuples representing the shortest path, or -1 if no path exists.
    """

    # WRITE YOUR CODE HERE
    output = []
    queue = []
    dist = {}
    prev = {}
    for i in graph:
        prev[i] = None
        if i == source:
            dist[i] = 0
            EnQueue(queue,i,0)
        else:
            dist[i] = math.inf
            EnQueue(queue,i,math.inf)
    while not IsEmpty(queue):
        q = DeQueue(queue)
        for i in graph[q]:
            if i[0] in dist:
                if dist[i[0]]>dist[q]+i[1]:
                    dist[i[0]] = dist[q]+i[1]
                    prev[i[0]] = q 
                    EnQueue(queue,i[0],dist[i[0]])
    
    
    def dhoondo(graph,s,d):
        for i in graph[s]:
            if i[0] == d:
                return i[1]
            


    print(dist, prev)
    dest = destination
    to_stop = prev[dest]
    if to_stop == None:
        return -1
    # dest = destination
    # to_stop = prev[destination]
    while to_stop != None:
        w = dhoondo(graph,to_stop, dest)
        if w !=None:
            output.append((to_stop, dest, w))
        dest = to_stop
        to_stop = prev[dest]
    # output.append((destination,w[0],w[1]))

    output.reverse()
    print(graph, source, destination)
    if output == []:
        return -1
    return(output)



    # output.reverse()
    # print(output)
    # if output != []:
    #     return(output)
    # else:
    #     return -1


#############################################################################
# Let's test your code... Run your code file and check manually whether the #
# code is running as expected...                                            #
#############################################################################
if __name__ == "__main__":
    graph = {
        'A': [('D', 2), ('E', 6), ('B', 7)], 
        'B': [('C', 3), ('A', 7)], 
        'C': [('B', 3), ('D', 2), ('G', 2)], 
        'D': [('A', 2), ('C', 2), ('F', 8)], 
        'E': [('A', 6), ('F', 9)], 
        'F': [('D', 8), ('E', 9), ('G', 4)], 
        'G': [('C', 2), ('F', 4)]
    }

    print(GetShortestPath(graph, 'A', 'G'))
    ''' Should print:
    [('A', 'D', 2), ('D', 'C', 2), ('C', 'G', 2)]
    '''

    print(GetShortestPath(graph, 'A', 'C'))
    ''' Should print:
    [('A', 'D', 2), ('D', 'C', 2)]
    '''

    print(GetShortestPath(graph, 'A', 'D'))
    ''' Should print:
    [('A', 'D', 2)]
    '''

    graph = {'A': [('B', 4)], 'B': [('A', 4), ('C', 2)], 'C': []}
    print(GetShortestPath(graph, "A", "C"))


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q2.py