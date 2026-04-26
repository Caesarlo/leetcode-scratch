from typing import List, Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.pre: Optional[TreeNode] = None
        self.count = 0
        self.maxCount = 0
        self.res = []
        self.traverse(root)
        return self.res

    def traverse(self, cur: Optional[TreeNode]):
        if not cur:
            return None
        self.traverse(cur.left)
        if self.pre is None:
            self.count = 1
        elif self.pre.val == cur.val:
            self.count += 1
        else:
            self.count = 1
        self.pre = cur
        if self.count == self.maxCount:
            self.res.append(cur.val)
        if self.count > self.maxCount:
            self.maxCount = self.count
            self.res.clear()
            self.res.append(cur.val)
        self.traverse(cur.right)

        return
