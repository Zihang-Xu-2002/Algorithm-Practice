from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(root, head):
            if head is None:
                return True
            if root is None:
                return False
            if root.val != head.val:
                return False

            return dfs(root.left, head.next) or dfs(root.right, head.next)
        def traverse(root):
            if root is None:
                return False
            
            # Check if the current tree node can be the start of the linked list path
            return dfs(root, head) or traverse(root.left) or traverse(root.right)
        
        return traverse(root)