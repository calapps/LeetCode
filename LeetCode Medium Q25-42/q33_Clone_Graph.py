# https://leetcode.com/problems/clone-graph/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # each node has a unique value, and we are passed in a graph and want to clone it
        # want to return the copy of the given node as a refernce to the cloned graph
        
        # so we will use DFS recursion and traverse each node once so it would be O(n)
        
        # the unique thing in this problem is because we have each node have a unique val and therefore num
        # we can map a val to a node: {1:node(1), ...}
        # for this problem we can use a hashmap for above and also check if a node is traversed or not through
        # checking if that node.val is in the set
        # and sometimes you don't have to call dfs iteratively
        # remember to TAKE NOTE OF EVERY SINGLE PIECE OF INFO BECUASE ITS THERE FOR A REASON

        if not node:
            return node
        
        visited = set()
        res = {}
        
        # for dfs, we never preset the first thing to be true to not, etc because we do it in dfs, so
        # don't create the first node here, create the first clone node in dfs and return it.
        # since this is a special case and we call dfs, we want to call it once, if it was
        # not make a brand new graph, then we would just want to iterate over it's neighbors I guess
        return self.dfs(node, visited, res)

    def dfs(self, node, visited, res):
        
        # basecase would be if it's already visited (typical dfs basecase)
        # so we check if it's already visited and if so return the code of that node we are on
        if node.val in visited:
            return res[node]

        # else create the node if it doesn't exist
        # and add it into our visited
        visited.add(node.val)

        if node not in res.keys():
            res[node] = Node(node.val)

        # iterate over the original node's neighbors and do recursive dfs
        # and check if ... the second line here is very confusing because
        # how do we know if objects are equal to eachother or not WTF just handwave this logic i guess
        for n in node.neighbors:
            if n not in res[node].neighbors:
                res[node].neighbors.append(self.dfs(n, visited, res))

        # return current node clone
        return res[node]


# I need to make a system where we can check if a new node is in the set given an old node, and this is the main
# thing I had trouble with: how to have the new node, and old node in the same pass in, and also how do we check
# if it's visited already (your previous way of checking was good but the set() way is better)
# so the main thing for here is that we can do {original node: new node} as a hashmap, and pass that around
# 



