from ast import List
from logging import root
from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution0:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.vec = []

        self.isValid(root)

        for i in range(1, len(self.vec)):
            if self.vec[i] <= self.vec[i-1]:
                return False

        return True

    def isValid(self, node: Optional[TreeNode]):
        if node == None:
            return

        self.isValid(node.left)
        self.vec.append(node.val)
        self.isValid(node.right)


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.maxVal = float('-inf')
        return self.isValid(root)

    def isValid(self, node: Optional[TreeNode]):
        if node == None:
            return True

        left = self.isValid(node.left)
        if node.val > self.maxVal:
            self.maxVal = node.val
        else:
            return False
        right = self.isValid(node.right)

        return left and right
