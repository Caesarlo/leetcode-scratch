from platform import node
from tkinter import NO
from typing import Optional
from collections import deque


# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution0:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        ans = root.val

        while queue:
            size = len(queue)

            for i in range(size):
                node = queue.popleft()

                if i == 0:
                    ans = node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return ans


class Solution:

    def __init__(self):
        self.max_depth = float('-inf')
        self.res: int

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        self.traversal(root, 1)
        return self.res

    def traversal(self, node: Optional[TreeNode], depth: int):
        if node.left == None and node.right == None:
            if depth > self.max_depth:
                self.max_depth = depth
                self.res = node.val

        if node.left:
            depth += 1
            self.traversal(node.left, depth)
            depth -= 1
        if node.right:
            depth += 1
            self.traversal(node.right, depth)
            depth -= 1
