# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        
        if not root: return root 

        minVal = min(p.val, q.val)
        maxVal = max(p.val, q.val)

        if minVal > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        if maxVal < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        return root 


# you made the mistake of not leveraging the pwoer of a bst, only a bt...
# reading comprehension please
