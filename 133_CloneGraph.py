# Definition for a undirected graph node
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        def clone_dfs(node_seed,graph,visited ):
            if node_seed.label in visited:
                return
            visited.add(node_seed.label)
            if node_seed.label not in graph :
                graph[node_seed.label] = UndirectedGraphNode(node_seed.label)
            node_next = graph[node_seed.label]

            for value in node_seed.neighbors:
                if value.label not in graph:
                    graph[value.label] = UndirectedGraphNode(value.label)
                node_next.neighbors.append(graph[value.label])
                clone_dfs(value, graph, visited)
            return node_next

        if not node :
            return None
        graph = {}
        visited = set()
        return  clone_dfs(node,graph,visited )

if __name__ == '__main__':

    node1 = UndirectedGraphNode(0)
    node2 = UndirectedGraphNode(1)
    node3 = UndirectedGraphNode(2)

    node1.neighbors = [node2,node3]
    node2.neighbors = [node3]
    node3.neighbors = [node3]


    k = Solution()
    print node1.label

    r= k.cloneGraph(node1)
