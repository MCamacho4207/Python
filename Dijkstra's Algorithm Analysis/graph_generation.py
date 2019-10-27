import timeit
import numpy
import networkx
import xlwt

def generate_timings(myDijkstra, ID, small_dataset=False):
    """
    Generate timing data
    """
    numpy.random.seed(ID)
    if small_dataset:
        clique_sizes = [i for i in range(4, 9, 4)]
        number_of_cliques = [i for i in range(2, 10, 2)]
    else:
#        clique_sizes = [i for i in range(4, 30, 4)]
#        number_of_cliques = [i for i in range(2, 20, 2)]
        clique_sizes = [i for i in range(4, 13, 4)]
        number_of_cliques = [i for i in range(2, 10, 2)]
    graph_n = []
    graph_m = []
    times = []
    
    number_of_graphs = len(number_of_cliques)*len(clique_sizes)
    print("Your implementation named", myDijkstra.__name__, \
          "will be run on a total of", number_of_graphs, "graphs")
    graph_cntr = 0
    
    if networkx.__version__[0] == '2':
        for n_cliques in number_of_cliques:
            for clique_size in clique_sizes:
                graph_cntr += 1
                # Construct the networkx graph
                graph = networkx.connected_caveman_graph(n_cliques, clique_size)
                assert(networkx.is_connected(graph))
                this_graph_n = len(graph.nodes())
                this_graph_m = len(graph.edges())
                graph_n.append(this_graph_n)
                graph_m.append(this_graph_m)
                print("Working on graph number", graph_cntr, \
                      "of size n = |V| =", this_graph_n, "and m = |A| =", \
                      this_graph_m)
                # Construct the successors list for the dijkstra function
                successors = []
                for _ in graph.adjacency():
                    successors.append(dict())
                for start_node, adj_dict in graph.adjacency():
                    for end_node in list(adj_dict.keys()):
                        # Add in a random distance
                        distance = numpy.random.randint(1, 10)
                        successors[start_node][end_node] = distance
                        successors[end_node][start_node] = distance
                # Call the function
                this_graph_times = []
                for n in range(1, this_graph_n):
                    t = timeit.Timer(lambda: myDijkstra(successors, n))
                    this_graph_times.append(t.timeit(number=3))
                times.append(this_graph_times)
    else: # NetworkX version is less than version 2
        for n_cliques in number_of_cliques:
            for clique_size in clique_sizes:
                # Construct the networkx graph
                graph = networkx.connected_caveman_graph(n_cliques, clique_size)            
                assert(networkx.is_connected(graph))
                this_graph_n = len(graph.nodes())
                this_graph_m = len(graph.edges())
                graph_n.append(this_graph_n)
                graph_m.append(this_graph_m)
                print("Working on graph number", graph_cntr, \
                      " of size n = |V| = ", this_graph_n, " and m = |A| =", \
                      this_graph_m)
                # Construct the successors list for the dijkstra function
                successors = []
                for _ in graph.adjacency_list():
                    successors.append(dict())
                for start_node, adj in enumerate(graph.adjacency_list()):
                    for end_node in adj:
                        # Add in a random distance
                        distance = numpy.random.randint(1, 10)
                        successors[start_node][end_node] = distance
                        successors[end_node][start_node] = distance
                # Call the function
                this_graph_times = []
                for n in range(1, this_graph_n):
                    t = timeit.Timer(lambda: myDijkstra(successors, n))
                    this_graph_times.append(t.timeit(number=3))
                times.append(this_graph_times)
    # Now write it out to an Excel workbook
    book = xlwt.Workbook()
    sheet = book.add_sheet("Data")
    sheet.row(0).write(0, "n = |V|")
    sheet.row(1).write(0, "m = |A|")
    sheet.row(2).write(0, "Dijkstra times [microsec]")
    #for col, g_size in enumerate(graph_n):
    for col, g_n, g_m in zip(range(0,len(graph_n)), graph_n, graph_m):
        print(col, g_n, g_m)
        sheet.row(0).write(col+1, g_n)
        sheet.row(1).write(col+1, g_m)
        for row, t in enumerate(times[col]):
            sheet.row(row+2).write(col+1, t)
    #book.save('dijkstra_data.xls')
    #book.save(xls_filename)
    book.save(myDijkstra.__name__ + "_data.xls")
    # Return the data we wrote to the file, just in case
    return graph_n, graph_m, times


#def generate_data(myDijkstra, ID, csv_filename):
#    """
#    Generate data files
#    
#    Parameters
#    ----------
#    
#    Returns
#    -------
#    """
#    
#    # Set the random seed from the ID
#    numpy.random.seed(ID)
#    clique_sizes = [i for i in range(4, 30, 4)]
#    number_of_cliques = [i for i in range(2, 20, 2)]
#    graph_size = []
#    distances = []
#    for n_cliques in number_of_cliques:
##        print('n_clique', n_cliques)
#        for clique_size in clique_sizes:
##            print('clique_size', clique_size)
#            # Construct the networkx graph
#            graph = networkx.connected_caveman_graph(n_cliques, clique_size)
#            assert(networkx.is_connected(graph))
#            this_graph_size = len(graph.nodes())
#            graph_size.append(this_graph_size)
#            # Construct the adjacency list for the dijkstra function
#            adjacency = []
#            for _ in graph.adjacency_list():
#                adjacency.append(dict())
#            for start_node, adj in enumerate(graph.adjacency_list()):
#                for end_node in adj:
#                    # Add in a random distance
#                    distance = numpy.random.randint(1, 10)
#                    adjacency[start_node][end_node] = distance
#                    adjacency[end_node][start_node] = distance
#            # Call the function
#            this_graph_distances = []
#            for n in range(1, this_graph_size):
##                print('node', n, 'of', this_graph_size)
#                this_graph_distances.append(myDijkstra(adjacency, n))
#            distances.append(this_graph_distances)
#    # Average over the distances
#    average_distances = numpy.zeros(len(graph_size))
#    for i, ds in enumerate(distances):
#        average_distances[i] = numpy.mean(ds)
#    output_array = numpy.zeros((len(graph_size), 4))
#    for i, n_cliques in enumerate(number_of_cliques):
#        for j, clique_size in enumerate(clique_sizes):
#            k = i*len(clique_sizes) + j
#            output_array[k, 0] = n_cliques
#            output_array[k, 1] = clique_size
#            output_array[k, 2] = graph_size[k]
#            output_array[k, 3] = average_distances[k]
#    header = """
#    Dijkstra data set
#    Stores the average distance between node 0 and all other nodes
#    in a random connected graph depending on two parameters, the number
#    of cliques, and the size of each clique.
#    
#    Column 0: Number of cliques
#    Column 1: Size of each clique
#    Column 2: Total graph size
#    Column 3: Average distance from node 0 to other nodes
#    
#    Student ID: {}
#    """.format(ID)
#    #csv_filename = 'dijkstra_data.csv'
#    numpy.savetxt(csv_filename, output_array, header = header)
#    return graph_size, average_distances
