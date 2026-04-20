from typing import Optional, List
from collections import deque

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        que: deque[TreeNode] = deque()
        res = []
        size = 0

        if root:
            que.append(root)

        while que:
            size = len(que)
            temp_res = []
            while size:
                cur = que.popleft()
                temp_res.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
                size -= 1

            res.append(temp_res)
        return res
