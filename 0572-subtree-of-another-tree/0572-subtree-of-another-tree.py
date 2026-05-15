# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        return (s.val == t.val and
                self.isSameTree(s.left, t.left) and
                self.isSameTree(s.right, t.right))
    def isSubtree(self, root, subRoot):
        if not subRoot:
            return True   # empty tree is always a subtree
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))
        