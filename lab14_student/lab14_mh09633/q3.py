from HelperFunctions import *
from q2 import GetShortestPath
from q1 import *
    
def GetShortestPathGrid(grid, source, destination):
    """
    Finds the shortest path from source to destination in a grid using Dijkstra's algorithm.

    Args:
        grid (list): 2D matrix with obstacles (-1) and free spaces (1).
        source (tuple): Starting grid coordinates (i, j).
        destination (tuple): Target grid coordinates (i, j).

    Returns:
        list: Shortest path as [(start, end, weight), ...], or -1 if no path exists.
    """
    
    # WRITE YOUR CODE HERE
    G = {}
    Nodes = []
    Edges = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1: 
                Nodes.append((i,j))
                if (j+1) <= (len(grid[0])-1):
                    if grid[i][j+1] == 1:
                        Edges.append(((i,j),(i,j+1),1))
                if (i+1) <= (len(grid)-1):
                    if grid[i+1][j] == 1:
                        Edges.append(((i,j),(i+1,j),1))
                if (j-1) >=0:
                    if grid[i][j-1] == 1:
                        Edges.append(((i,j),(i,j-1),1))
                if (i-1)>=0:
                    Edges.append(((i,j),(i-1,j),1))

    AddNodes(G,Nodes)
    AddEdges(G, Edges,True)

    # print(G)
    # print(Nodes)
    # print(Edges)

    return GetShortestPath(G,source,destination)




            
            





#############################################################################
# Let's test your code... Run your code file and check manually whether the #
# code is running as expected...                                            #
#############################################################################
if __name__ == "__main__":
    grid =[[1, 1, 1], [-1, 1, 1], [1, -1, 1]]
    source = (0, 0)
    destination = (2, 2)
    print(GetShortestPathGrid(grid, source, destination))
    ''' Should print ANY ONE of the below shortest paths:
    [((0, 0), (0, 1), 1), ((0, 1), (1, 1), 1), ((1, 1), (1, 2), 1), ((1, 2), (2, 2), 1)]
    [((0, 0), (0, 1), 1), ((0, 1), (0, 2), 1), ((0, 2), (1, 2), 1), ((1, 2), (2, 2), 1)]
    '''

    grid = [[1, 1], [-1, 1]]
    source = (0, 0)
    destination = (1, 1)
    print(GetShortestPathGrid(grid, source, destination))
    ''' Should print:
    [((0, 0), (0, 1), 1), ((0, 1), (1, 1), 1)]
    '''

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q3.py