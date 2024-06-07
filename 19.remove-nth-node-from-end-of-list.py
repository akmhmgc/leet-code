#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # reverse
        prev, cur = None, head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        
        # remove nth node and reverse
        cur = prev
        prev = None
        i = 0
        while cur:
            i += 1
            next = cur.next
            if i == n:
                cur.next = None
            else:
                cur.next = prev
                prev = cur
            cur = next
        return prev
# @lc code=end

