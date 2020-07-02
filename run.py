# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)
print("-------------FIFO---------------")
print(search.breadth_first_graph_search(ab).path())
print("-------------STACK---------------")
print(search.depth_first_graph_search(ab).path())
print("-------------RamiAcot---------------")
print(search.ra_graph_search(ab).path())
print("-------------RamiAcotSub---------------")
print(search.ras_graph_search(ab).path())


# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450

