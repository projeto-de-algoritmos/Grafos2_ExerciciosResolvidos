from typing import List
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

      graph = {}
        for u, v, w in times:
            if u not in graph:
                graph[u] = []
            graph[u].append((v, w))
        
        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        
        pq = [(0, k)]
        
        while pq:
            time, node = heapq.heappop(pq)
            if time > dist[node]:
                continue
            if node in graph:
                for neighbor, weight in graph[node]:
                    new_time = time + weight
                    if new_time < dist[neighbor]:
                        dist[neighbor] = new_time
                        heapq.heappush(pq, (new_time, neighbor))
        
        max_time = max(dist[1:])
        
        return max_time if max_time < float('inf') else -1
