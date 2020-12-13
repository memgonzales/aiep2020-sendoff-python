# Solution to Session 10 Problem 10
# 2020 AIEP Send-off
# @author Mark Edward M. Gonzales
# @date   November 4, 2020

import collections
from collections import defaultdict, deque

UNIT_WEIGHT = 6

def to_adj_list(edges):
    adj_list = defaultdict(list)

    for edge in edges:
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])
    
    return adj_list


def bfs_shortest(edges, start_vertex, num_vertices):
    adj_list = to_adj_list(edges)
    
    visited = defaultdict(lambda : False)
    distances = defaultdict(lambda : -1)

    queue = deque()
    visited[start_vertex] = True
    queue.append(start_vertex)

    distances[start_vertex] = 0

    while queue:
        vertex = queue.popleft()

        for adj_vertex in adj_list[vertex]:
            if not visited[adj_vertex]:
                queue.append(adj_vertex)
                visited[adj_vertex] = True

                distances[adj_vertex] = distances[vertex] + UNIT_WEIGHT

    for i in range(1, num_vertices + 1):
        if i != start_vertex:
            print(distances[i], end = ' ')


num_test_cases = int(input())

for _ in range(num_test_cases):
    dimensions = list(map(int, input().split()))
    num_vertices = dimensions[0]
    num_edges = dimensions[1]

    edges = []
    for _ in range(num_edges):
        edge = list(map(int, input().split()))
        edges.append(edge)

    start_vertex = int(input())

    bfs_shortest(edges, start_vertex, num_vertices)
    print()   
