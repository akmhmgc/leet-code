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
        dummy = ListNode(0, head)
        first, second = dummy, head

        i = 0
        while i < n and second:
            i += 1
            second = second.next
        
        while second:
            first = first.next
            second = second.next

        first.next = first.next.next

        return dummy.next
# @lc code=end

