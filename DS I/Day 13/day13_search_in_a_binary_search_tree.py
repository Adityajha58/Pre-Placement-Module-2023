class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        
        while root:
            
            if val < root.val:
                root = root.left
            elif val > root.val:
                root = root.right
            else:
                return root