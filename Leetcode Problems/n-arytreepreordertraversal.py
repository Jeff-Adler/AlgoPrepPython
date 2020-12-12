"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:

        if root == None:
            return []

        preorder_list = []

        def dfs(node):

            preorder_list.append(node.val)

            if node:
                for child in node.children:
                    dfs(child)

        dfs(root)

        return preorder_list
