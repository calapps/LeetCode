# https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        
        if not root:
            return 
        
        tmp = root.left 
        root.left = root.right
        root.right = tmp 

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root 

# [1,2,3] => [1,3,2]
# [1,2,3,4,5,6,7] => [1,3,2,7,6,5,4]
# [] => [] 