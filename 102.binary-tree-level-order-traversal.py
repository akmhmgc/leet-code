#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        nodes = [root]
        while nodes:
            level = []
            for i in len(nodes):
                node = nodes.popleft()
                if node:
                    level.append(node.val)
                    nodes.append(node.left)
                    nodes.append(node.right)
            res.append(level)
        return res
# @lc code=end

