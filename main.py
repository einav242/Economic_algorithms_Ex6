from typing import List

import networkx as nx


def find_cycle_in_consumption_graph(allocation: List[List[float]]):
    g = nx.DiGraph()
    # add node for people
    for i in range(len(allocation)):
        g.add_node("person-" + str(i))
    # add node for item
    for i in range(len(allocation[0])):
        g.add_node("item-" + str(i))
    for i in range(len(allocation)):
        for j in range(len(allocation[i])):
            if allocation[i][j] > 0:
                node1 = "person-" + str(i)
                node2 = "item-" + str(j)
                g.add_edge(node1, node2)
    cycles = list(nx.cycle_basis(g.to_undirected()))
    ans = dict()
    count = 1
    if cycles:
        for cycle in cycles:
            ans["cycle " + str(count)] = cycle
            count += 1
        return ans
    print("No  cycle")


lst = [[1, 0, 0], [0, 0, 0.7], [0, 0, 0.3], [0, 1, 0]]
print("lst=", find_cycle_in_consumption_graph(lst))
lst2 = [[0.1, 0, 0.5], [0.9, 0.6, 0], [0, 0.4, 0.5]]
print("lst2= ", find_cycle_in_consumption_graph(lst2))
lst3 = [[0.1, 0.4, 0, 0], [0.9, 0.6, 0, 0], [0, 0, 0.5, 0.8], [0, 0, 0.5, 0.2]]
print("lst3= ", find_cycle_in_consumption_graph(lst3))
lst4 = [[0.1, 0.4, 0, 0], [0.9, 0.6, 0, 0], [0, 0, 0.5, 0.8], [0, 0, 0.5, 0.2]]
print("lst4= ", find_cycle_in_consumption_graph(lst4))
lst5 = [[0.1, 0.4, 0, 0], [0.9, 0.3, 0.3, 0], [0, 0.3, 0.4, 0.8], [0, 0, 0.3, 0.2]]
print("lst5= ", find_cycle_in_consumption_graph(lst5))
