# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root)

    def helper(self, root, floor=float("-inf"), ceil=float("inf")):

        if not root:
            return True

        if root.val <= floor or root.val >= ceil:
            return False
        
        return self.helper(root.left, floor, root.val) and self.helper(root.right, root.val, ceil)
