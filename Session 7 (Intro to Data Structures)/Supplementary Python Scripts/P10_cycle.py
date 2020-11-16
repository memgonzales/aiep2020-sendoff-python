# Solution to Session 7 Problem 10
# 2020 AIEP Send-off
# @author Mark Edward M. Gonzales
# @date   October 22, 2020

import collections
from collections import defaultdict

NO_PARENT = -1

class Graph:
    def __init__(self):
        self.adjacency_list = defaultdict(list)
        
    def add_edge(self, vertex1, vertex2, directed):
        self.adjacency_list[vertex1].append(vertex2)

        if not directed:
            self.adjacency_list[vertex2].append(vertex1)

    
    def has_cycle_helper(self, vertex, parent, visited):
        visited[vertex] = True

        for adjacent_vertex in self.adjacency_list[vertex]:
            if not visited[adjacent_vertex]:
                if self.has_cycle_helper(adjacent_vertex, vertex, visited):
                    return True
            elif adjacent_vertex != parent:
                return True

        return False
    

    def has_cycle(self):
        visited = collections.defaultdict(lambda: False)

        for vertex in self.adjacency_list.keys():
            if not visited[vertex]:
                if self.has_cycle_helper(vertex, NO_PARENT, visited):
                    return True

        return False


# Sample Runs
g = Graph()
g.add_edge(1, 2, False)
g.add_edge(1, 4, False)
g.add_edge(1, 7, False)
g.add_edge(2, 3, False)
g.add_edge(2, 5, False)
g.add_edge(3, 6, False)
g.add_edge(4, 7, False)
g.add_edge(5, 6, False)
g.add_edge(5, 7, False)
g.add_edge(6, 7, False)

print(g.has_cycle())

h = Graph()
h.add_edge(1, 2, False)
h.add_edge(2, 3, False)
h.add_edge(1, 7, False)
h.add_edge(7, 6, False)

print(h.has_cycle())
