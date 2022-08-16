class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s == None:
            return False
        if s.val == t.val:
            res = self.checkSubtree(s.left, t.left) and self.checkSubtree(s.right, t.right)
            if res == True:
                return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


    def checkSubtree(self, s, t):
        if s == None or t == None:
            if s != None or t != None:
                return False
            else:
                return True
        elif s.val == t.val:
            return self.checkSubtree(s.left, t.left) and self.checkSubtree(s.right, t.right)
        else:
            return False