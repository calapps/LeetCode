# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    maxPath = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.maxPath

    def helper(self, root):
        if not root:
            return 0

        left = self.helper(root.left)
        right = self.helper(root.right)

        self.maxPath = max(self.maxPath, left+right)

        return 1 + max(left, right)    
