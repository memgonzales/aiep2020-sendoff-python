# Solution to Session 7 Problem 11
# 2020 AIEP Send-off
# @author Mark Edward M. Gonzales
# @date   October 22, 2020

import collections
from collections import defaultdict


class Graph:
    def __init__(self):
        self.adjacency_list = defaultdict(list)
        
    def add_edge(self, vertex1, vertex2, directed):
        self.adjacency_list[vertex1].append(vertex2)

        if not directed:
            self.adjacency_list[vertex2].append(vertex1)
            
    def print_audience(self, vertex):
        visited = collections.defaultdict(lambda : False)
        queue = collections.deque()
        queue.append(vertex)
        visited[vertex] = True

        num_friends = len(self.adjacency_list[vertex])
        
        while queue:
            vertex = queue.popleft()
            print(vertex)

            if num_friends >= 0:
                for adjacent_vertex in self.adjacency_list[vertex]:
                    if not visited[adjacent_vertex]:
                        queue.append(adjacent_vertex)
                        visited[adjacent_vertex] = True

            num_friends = num_friends - 1
            
# Sample Run
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

g.print_audience(3)
