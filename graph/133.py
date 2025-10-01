# 133. Clone Graph



# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional, List
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''
        visited map - K: node, V: same copied node

        def bfs(starting node):
            start at 1
            new node: copy val and neighbors
            q.append(starting node)
            while q:
                go thru original graph and make copies of each node
                add copy to dict
                
        '''
        # empty case
        if not node:
            return None
        
        # acts as visited
        nodes = {}  # K: node, V: same copied node
        
        def bfs(start):
            q = deque()
            q.append(start)
            nodes[start] = Node(val=start.val)

            while len(q)>0:
                curr = q.popleft()
                for neighbor in curr.neighbors:
                    # if unique neighbor
                    if neighbor not in nodes:
                        # clone neighbor to dict
                        nodes[neighbor] = Node(val=neighbor.val)
                        # append to q
                        q.append(neighbor)
                    # outside of IF b/c we have bi-directional neighbors (non-unique)
                    nodes[curr].neighbors.append(nodes[neighbor])

        bfs(node)
        return nodes[node]