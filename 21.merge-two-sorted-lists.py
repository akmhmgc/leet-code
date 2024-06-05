#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1

        res, head1, head2 =  (list1, list1,list2) if list1.val <= list2.val else (list2, list2,list1)
        while head1 and head2:
            if not head1.next:
                head1.next = head2
                head1 = None
            elif head1.next.val >= head2.val:
                next = head1.next
                head1.next = head2
                head1 = head2
                head2 = next
            else:
                head1 = head1.next
        return res
# @lc code=end

