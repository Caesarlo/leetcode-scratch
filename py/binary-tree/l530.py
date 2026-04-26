from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.min_diff = float('inf')
        self.pre = None

        self.traversal(root)

        return self.min_diff

    def traversal(self, node: Optional[TreeNode]):
        if not node:
            return None

        self.traversal(node.left)

        if self.pre:
            self.min_diff = min(self.min_diff, abs(self.pre.val-node.val))
        self.pre = node

        self.traversal(node.right)
