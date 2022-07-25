class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        def fn(node): 
            if not node: return 
            ans.append(node.val)
            fn(node.left)
            fn(node.right)
            
        ans = []
        fn(root)
        return ans