class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        q = [root]

        while q:
            res.append(q[-1].val)
            q =  [child for node in q for child in (node.left, node.right) if child]
        
        return res