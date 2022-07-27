class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        
        if root is None:
            return TreeNode(val)
        
        current = root
        
        while current:
            if val < current.val:
                if current.left is None:
                    current.left = TreeNode(val)
                    break
                    
                current = current.left
            else:
                if current.right is None:
                    current.right = TreeNode(val)
                    break
                    
                current = current.right
        
        return root