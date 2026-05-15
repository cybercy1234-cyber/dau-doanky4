# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        result = []
        def dfs(node):
            if not node:
                return
            result.append(node.val)   # Visit root
            dfs(node.left)            # Traverse left
            dfs(node.right)           # Traverse right
        dfs(root)
        return result