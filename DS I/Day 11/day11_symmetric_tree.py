# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        dq = collections.deque([root.left, root.right])
        while dq:
            left, right = dq.popleft(), dq.pop()
            if not left and not right: continue
            if not left or not right: return False
            if left.val != right.val: return False
            dq.appendleft(left.left)
            dq.append(right.right)
            dq.appendleft(left.right)
            dq.append(right.left)
        return True