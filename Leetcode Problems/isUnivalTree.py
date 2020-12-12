# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:

        nodes = set()

        def preorderDFS(node):
            nodes.add(node.val)

            if node.left:
                preorderDFS(node.left)

            if node.right:
                preorderDFS(node.right)

        preorderDFS(root)

        if len(nodes) > 1:
            return False
        else:
            return True
