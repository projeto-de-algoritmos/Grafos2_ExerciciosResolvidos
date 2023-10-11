from typing import List

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        def find(parent, x):
            if parent[x] == -1:
                return x
            return find(parent, parent[x])
        
        def union(parent, x, y):
            root_x = find(parent, x)
            root_y = find(parent, y)
            if root_x != root_y:
                parent[root_x] = root_y
        
        n = len(edges)
        parent_candidates = [-1] * (n + 1)
        conflict = []
        second_edge = None

        for edge in edges:
            u, v = edge
            if parent_candidates[v] == -1:
                parent_candidates[v] = u
            else:
                conflict = [parent_candidates[v], v]
                second_edge = edge

        parent = [-1] * (n + 1)
        for edge in edges:
            if edge == second_edge:
                continue
            if find(parent, edge[0]) == find(parent, edge[1]):
                return conflict if conflict else edge
            union(parent, edge[0], edge[1])

        return second_edge
