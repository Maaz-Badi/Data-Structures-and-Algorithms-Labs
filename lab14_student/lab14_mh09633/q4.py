from HelperFunctions import *
from q2 import GetShortestPath

def GetShortestDistanceBetweenCities(source, destination):
    """
    Computes the shortest path between two cities using Dijkstra's algorithm.

    Reads the adjacency matrix from `connections.csv` and returns the shortest 
    path from `source` to `destination` as a list of tuples (start_city, end_city, distance), 
    or -1 if no path exists.

    Args:
        source (str): The starting city.
        destination (str): The destination city.

    Returns:
        list or int: Shortest path as a list of tuples (start_city, end_city, distance), 
                     or -1 if no path exists.
    """

    # WRITE YOUR CODE HERE
    G = {}
    rows = []
    with open('connections.csv', 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            rows.append(row)
    # print(header)
    # print(rows)
    list_ofNodes = header[1:len(header)]
    AddNodes(G,list_ofNodes)
    for i in rows:
        node = i[0]
        neigh = i[1:]
        for j in range(len(neigh)):
            if neigh[j] != "-1" and neigh[j] != "0":
                G[node].append((list_ofNodes[j], int(neigh[j])))

    # print(G)
    # return G
    return GetShortestPath(G,source,destination)


#############################################################################
# Let's test your code... Run your code file and check manually whether the #
# code is running as expected...                                            #
#############################################################################
if __name__ == "__main__":
    print(GetShortestDistanceBetweenCities("Islamabad",'Nathiagali'))   
    '''Should print:
    [('Islamabad', 'Murree', 49), ('Murree', 'Nathiagali', 36)]
    '''

    print(GetShortestDistanceBetweenCities('Islamabad', 'Naran'))
    ''' Should print: 
    [('Islamabad', 'Murree', 49), ('Murree', 'Nathiagali', 36), ('Nathiagali', 'Abbottabad', 34), 
     ('Abbottabad', 'Mansehra', 23), ('Mansehra', 'Balakot', 37), ('Balakot', 'Kaghan', 59), 
     ('Kaghan', 'Naran', 22)]
    '''
    
    print(GetShortestDistanceBetweenCities("Islamabad", "Murree"))
    ''' Should print:
    [('Islamabad', 'Murree', 49)]
    '''

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q4.py