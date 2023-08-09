# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        # the relationship in preorder and inorder is as follows:
        # for every item in preorder, it is sorted by the parent root level order first, and if we find that
        # root in the inorder array, we see that everything to it's left and right are to it's left and right
        # in the preorder array
        if not inorder or not preorder:
            return None

        print(preorder)
        print(inorder)
        print("")
        root = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])

        # first preorder means everything to the left of it, and inorder means
        # everything to the left of it in inorder
        # second preorder means everything to the right of it 
        # To make sense of preorder[1:idx+1], we know that for inorder, everything
        # to the left of preorder[0] belongs to the left of preorder in the inorder 
        # so the idx of preorder in inorder is also the legth of items that are to
        # the left of it, so then we just want the n length amount to the left of it
        # in preorder
        # ANOTHER THING YOU MUST REALIZE ABOUT THIS IS THAT NOT ONLY DOES
        # P = MLR, I = LMR, BUT ALSO THAT len(I[:M] == number of L in P)
        root.left = self.buildTree(preorder[1:idx+1], inorder[:idx])
        root.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])

        return root 

p = [3,9,20,15,7]
i = [9,3,15,20,7]

obj = Solution()
obj.buildTree(p,i) 