from collections import deque
from typing import List, Set

class Solution:
    def __edgesToDict(self, edges: List[List[int]], n: int):
        graph = {i: [] for i in range(n)}

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        return graph

    def __bfsAlgorithm(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = self.__edgesToDict(edges, n)
        searchQueue = deque()
        searchQueue.append(source)
        checked = []
        while searchQueue:
            source = searchQueue.popleft()
            if destination in graph[source]:
                return True
            checked.append(source)
            searchQueue += graph[source]
            
        return True
    
    def __deepFirstSearch(self, graph: dict[int, List[int]], source, destination, visited: Set):
        if source not in visited:
            visited.add(source)

            for neighbor in graph[source]:
                if neighbor == destination:
                    return True
                if neighbor not in visited:
                    if self.__deepFirstSearch(graph, neighbor, destination, visited):
                        return True
            return False
    
    def __dfsAlgorithm(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = self.__edgesToDict(edges, n)
        visited = set([])
        return self.__deepFirstSearch(graph, source, destination,visited)

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if destination > n - 1 or len(edges) == 0: 
            return False
        if source == destination:
            return True
        return self.__dfsAlgorithm(n, edges, source, destination)

solution = Solution()
n = 6
edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
source = 0
destination = 5
print(solution.validPath(n=n, source=source, destination=destination, edges=edges))
