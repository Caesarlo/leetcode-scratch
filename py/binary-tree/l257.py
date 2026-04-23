from typing import Optional, List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        path = []
        res = []
        self.get_path(root, path, res)
        return res

    def get_path(self, node: Optional[TreeNode], path: List[int], res: List[str]):
        path.append(node.val)
        if node.left == None and node.right == None:
            cur = '->'.join(map(str, path))
            res.append(cur)

        if node.left:
            left = self.get_path(node.left, path, res)
            path.pop()
        if node.right:
            right = self.get_path(node.right, path, res)
            path.pop()
