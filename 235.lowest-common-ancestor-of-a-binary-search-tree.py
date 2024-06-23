#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        tail = root
        if p.val > q.val: p, q = q, p
        while True:
            if p.val <= tail.val and tail.val <= q.val:
                return tail
            elif p.val < tail.val and q.val < tail.val:
                tail = tail.left
            else:
                tail = tail.right
# @lc code=end

