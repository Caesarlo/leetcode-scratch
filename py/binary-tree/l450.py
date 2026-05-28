from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None:
            return None

        if root.val == key:
            if root.left == None and root.right == None:
                return None
            elif root.left != None and root.right == None:
                return root.left
            elif root.left == None and root.right != None:
                return root.right
            else:
                cur = root.right
                while cur.left:
                    cur = cur.left
                cur.left = root.left
                return root.right
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        if key > root.val:
            root.right = self.deleteNode(root.right, key)

        return root
