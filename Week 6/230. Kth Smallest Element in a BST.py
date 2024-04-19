class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        results = []
        def inorder(node):
            if node is None:
                return

            inorder(node.left)
            results.append(node.val)
            inorder(node.right)

        inorder(root)
        print(k)
        
        return results[k-1]