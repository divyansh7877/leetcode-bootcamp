# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base Case
        if root is None:
            return None

        if root == q or root == p: 
            return root
        
        foundInLeft = self.lowestCommonAncestor(root.left, p, q)
        
        foundInRight = self.lowestCommonAncestor(root.right, p, q)
        
        if not foundInLeft: 
            return foundInRight
        
        if not foundInRight: 
            return foundInLeft
        
        return root
        
