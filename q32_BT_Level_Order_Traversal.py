# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root: return []

        res = [[root.val]]
        q = deque([root])

        while q:
            qlen = len(q)
            holder = []
            for _ in range(qlen):
                node = q.popleft()

                if node.left:
                    holder.append(node.left.val)
                    q.append(node.left)
                
                if node.right:
                    holder.append(node.right.val)
                    q.append(node.right)
                

            if holder:
                res.append(holder)

        return res