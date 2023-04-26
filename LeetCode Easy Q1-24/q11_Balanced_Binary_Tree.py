# https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    res = True 

    def isBalanced(self, root):
        self.helper(root)
        return self.res 

    def helper(self, root):
        if not root:
            return 0 
        
        left = self.helper(root.left)
        right = self.helper(root.right)

        if abs(left-right) > 2:
            self.res = False
        
        return 1 + max(left, right)

# tree = []
# tree = [1,2,None,3,4,5]
# r = 1, l = 3, return false 
# tree = [1,2,3,4] =2-1 == 1 so true 
# tree = [3,9,20,null,null,15,7],
# 