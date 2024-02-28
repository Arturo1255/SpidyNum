import networkx as nx

def createDict(filename):
    # Stores the names of the character and stores them in a dictionary where the key is the id and the value is the name
    dictionary = {}
    with open(filename, 'r') as file:
        for i, line in enumerate(file):
            if i == 6486:
                break
            words = line.split()
            key = words[0]
            value = words[1].strip('"')
            dictionary.update({key: value})
    return dictionary


def createGraph(fileName):
    # Read file
    with open(fileName, "r") as f:
        lines = f.readlines()

    # Create graph
    G = nx.Graph()
    foundEdgeList = False

    # Add nodes
    for line in lines:
        if foundEdgeList:
            # Split the node IDs in the line
            num_strings = line.split()
            # Create a list that holds all the node IDs
            num_list = [int(num) for num in num_strings]
            for nodeID in num_list:
                # Add an edge between the first node in the list and every other node in the list
                G.add_edge(num_list[0], nodeID)

        if "*Edgeslist" in line:
            foundEdgeList = True
        else:
            # Create node and store the name of the node
            parts = line.strip().split(" ")
            G.add_node(int(parts[0]), name=" ".join(parts[1:]))
    f.close()
    return G


def bfs_shortest_path(graph, start, end):
    comparisons = 0
    assignments = 0
    # Create the queue
    queue = [(start, [start])]
    # Store the nodes that have been visited
    visited = set()

    while queue:
        (node, path) = queue.pop(0)
        visited.add(node)

        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                comparisons += 1
                if neighbor == end:
                    # If the neighbor is the end node, return the path to it
                    return path + [neighbor] , comparisons, assignments
                else:
                    # Add the neighbor to the queue with its path
                    assignments += 2
                    queue.append((neighbor, path + [neighbor]))
                    # Add the node to visited
                    visited.add(neighbor)

    return -1, comparisons, assignments


def calculateSpidyNum(graph, char, char2):
    # Holds the comic count
    comicCount = 0
    # Calculates and store the path between the two characters
    path, comparisons, assignments = bfs_shortest_path(graph, char, char2)

    # Check the path for comic book nodes

    if path == -1:
        return ">6"
    else:
        for node in path:
            if node < 6487:
                # If comic book node is found add one to comic count
                comicCount += 1
            return len(path) - comicCount



def MarvelNetwork(graph, names):
    # Print out the spidy numbers for all characters
    for i in range(1, 6487):
        print(i, " ", names[str(i)], " ", calculateSpidyNum(graph, 5306, i))



def main():
    marvel = createDict("porgat.txt")
    MarvelGraph = createGraph("porgat.txt")
    MarvelNetwork(MarvelGraph, marvel)

    return 0


main()







