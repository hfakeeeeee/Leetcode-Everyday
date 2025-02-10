import collections
import heapq

def maxProbability(n, edges, succProb, start_node, end_node):
    graph = collections.defaultdict(dict)

    for (source, dest), prob in zip(edges, succProb):
        graph[source][dest] = prob
        graph[dest][source] = prob

    heap = []
    heapq.heapify(heap)
    heapq.heappush(heap, (1, start_node))

    visited = set()

    while heap:
        node_prob, node = heapq.heappop(heap)
        if node == end_node:
            return abs(node_prob)

        visited.add(node)

        for child in graph[node]:
            if child not in visited:
                heapq.heappush(heap, (-abs(node_prob) * graph[node][child] ,child))

    return 0
           

if __name__ == "__main__":
    n = 5
    edges = [[1,4],[2,4],[0,4],[0,3],[0,2],[2,3]]
    succProb = [0.37,0.17,0.93,0.23,0.39,0.04]
    start = 3
    end = 4
    print(maxProbability(n, edges, succProb, start, end))