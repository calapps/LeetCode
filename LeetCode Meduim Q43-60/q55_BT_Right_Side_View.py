# https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        res = [root.val]

        q = deque([root])

        while q:
            rightMost = None
            for _ in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                    rightMost = node.left.val
                
                if node.right:
                    q.append(node.right)
                    rightMost = node.right.val
            
            if rightMost != None:
                res.append(rightMost)
        
        return res
