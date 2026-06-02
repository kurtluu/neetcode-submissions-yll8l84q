"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        clones = {} # original -> clone

        def dfs(og):
            # if og is already in hashMap, return it's clone
            if og in clones:
                return clones[og]

            # make a copy and register it 
            copy = Node(og.val)
            clones[og] = copy 

            # append the copy of each neighbors from the original neighbors
            for n in og.neighbors:
                copy.neighbors.append(dfs(n))

            return copy
        
        return dfs(node)




            

