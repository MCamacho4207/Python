def dijkstra1(successors, other_node):
    """
        Stub of Dijkstra's algorithm

        Parameters
        ----------
        successors : a list of dictionaries, encoding the "successors list" (seen in the lectures)
        other_node : index (an int) of the "target" node "t"

        Returns
        -------
        L[other_node] : the shortest path length from 1 to other_node

        """
    # initialize counter variable
    i = 0

    # store in a convenient variable (n) the number of nodes |V| in the graph
    n = len(successors)

    # initialize the set S of nodes currently reached with a shortest path
    S = []
    S.append(0)

    """initialize the data structure L; for any index i, L[i] contains the shortest path length from
    0 to i (if a 0--i path has already been found); we use a dictionary"""

    L = dict()
    L[0] = 0

    """initialize the data structure P; for any index i, P[i] contains the predecessor of a
    shortest 0--i path (if it has already been found); we use, again, a dictionary
    NOTE: is this structure really needed if we are only required to output the length
    of a shortest path, rather than a shortest path itself (i.e., a list of arcs)?"""
    P = dict()
    P[0] = '-'

    # the algorithm iterates until all nodes have been reached (i.e., until len(S) = |V|)
    while len(S) < n:
        forwardstar = []
        for node_fin in S:
            connected_nodes = successors[node_fin].keys()
            for node in connected_nodes:
                forwardstar.append([node_fin, node, successors[node_fin][node]])
                list_to_remove = []
        for arc_set in forwardstar:
            for value in S:
                if value == arc_set[1]:
                    list_to_remove.append(arc_set)
                    break
        for item in list_to_remove:
            forwardstar.remove(item)
        length_list = []
        a = 0
        for arc_set in forwardstar:
            length_list.append([L[arc_set[0]] + arc_set[2], a])
            a = a + 1
        while len(length_list) > 1:
            if length_list[0][0] < length_list[1][0]:
                length_list.remove(length_list[1])
            else:
                length_list.remove(length_list[0])
        correct_arc = forwardstar[length_list[0][1]]
        if correct_arc[1] in L.keys():
            if length_list[0][0] < L[correct_arc[1]]:
                L[correct_arc[1]] = length_list[0][0]
        else:
            L[correct_arc[1]] = length_list[0][0]
        P[correct_arc[1]] = correct_arc[0]
        if S.count(correct_arc[1]) == 0:
            S.append(correct_arc[1])

    return 7


def dijkstra2(successors, other_node):
    """
    Stub of Dijkstra's algorithm

    Parameters
    ----------
    successors : a list of dictionaries, encoding the "successors list" (seen in the lectures)
    other_node : index (an int) of the "target" node "t"

    Returns
    -------
    L[other_node] : the shortest path length from 1 to other_node

    """
    # initialize counter variable
    i = 0

    # store in a convenient variable (n) the number of nodes |V| in the graph
    n = len(successors)

    # initialize the set S of nodes currently reached with a shortest path
    S = []
    S.append(0)

    """initialize the data structure L; for any index i, L[i] contains the shortest path length from
    0 to i (if a 0--i path has already been found); we use a dictionary"""

    L = dict()
    L[0] = 0

    """initialize the data structure P; for any index i, P[i] contains the predecessor of a
    shortest 0--i path (if it has already been found); we use, again, a dictionary
    NOTE: is this structure really needed if we are only required to output the length
    of a shortest path, rather than a shortest path itself (i.e., a list of arcs)?"""
    P = dict()
    P[0] = '-'

    # the algorithm iterates until all nodes have been reached (i.e., until len(S) = |V|)
    while len(S) < n:
        """initialize appropriate variables to store the pair (v,w) achieving the smallest
        value of L[v] + l_{vw}"""

        # WRITE CODE HERE!
        forwardstar = []
        for node_fin in S:

            connected_nodes = successors[node_fin].keys()

            for node in connected_nodes:
                forwardstar.append([node_fin, node, successors[node_fin][node]])

        list_to_remove = []

        for arc_set in forwardstar:

            # print(arc_set[1])
            for value in S:

                # print(value, " ", arc_set[1])
                if value == arc_set[1]:
                    # print("removed")
                    list_to_remove.append(arc_set)
                    break
        for item in list_to_remove:
            forwardstar.remove(item)

        """we have now to loop over all arcs (v,w) in the cut induced by S, checking whether
        L[v] + lvw is smaller than the smallest value thus found, updating, if that is
        the case, our guess on the pair (v,w) minimizing L[v] + l_{vw};
        we can use two nested loops for this:
        * one going over all nodes v in S
        * one over all successors w of v, skipping any nodes w which are in S
        (as, if both v and w are in S, (v,w) is not in the cut induced by S);
        you can use the snippet provided in coursework.pdf to loop over the
        successors of node v in the internal loop"""

        # WRITE CODE HERE!

        length_list = []
        a = 0

        for arc_set in forwardstar:
            length_list.append([L[arc_set[0]] + arc_set[2], a])
            a = a + 1

        while len(length_list) > 1:
            if length_list[0][0] < length_list[1][0]:
                length_list.remove(length_list[1])
            else:
                length_list.remove(length_list[0])

        """at the end of the two nested loops,
        we should update L, P, and S with the new node just reached
        """
        correct_arc = forwardstar[length_list[0][1]]
        if correct_arc[1] in L.keys():
            if length_list[0][0] < L[correct_arc[1]]:
                L[correct_arc[1]] = length_list[0][0]
        else:
            L[correct_arc[1]] = length_list[0][0]

        P[correct_arc[1]] = correct_arc[0]

        if S.count(correct_arc[1]) == 0:
            S.append(correct_arc[1])

        a = 0
        length_list.clear()
        forwardstar.clear()
        list_to_remove.clear()
        for number in L:
            if number == other_node:
                return L[other_node]

    return L[other_node]


if __name__ == "__main__":

    # the successors list for the graph in coursework.pdf
    successors = [{1: 2, 2: 5}, {2: 3}, {3: 4}, {0: 21, 1: 8}]

    #print(dijkstra1_stub(successors, 3))

    """we test our algorithm, running it on "successors" for all possible
    target nodes"""
    for other_node in range(1, 4):

        print(dijkstra2(successors, other_node))

    """we supply our implementation 'dijkstra1_stub' to 'generate_timings', together
    with our ID number"""
    #graph_ns, graph_ms, times = graph_generation.generate_timings(dijkstra1, 29428211)
