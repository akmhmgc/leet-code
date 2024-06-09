#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # edge case
        if not lists or len(lists) == 0: return None

        # implement merge sort
        while len(lists) > 0:
            mergedLists = []
            for i in range(0, len(lists), 2):
               list1 = lists[i]
               list2 = lists[i + 1] if (i + 1) < len(lists) else None
               mergedLists.append(self.mergeList(list1, list2))
            lists = mergedLists
        return lists[0]
    

    def mergeList(self, li1, li2):
        dummy = ListNode()
        tail = dummy

        while li1 and li2:
            if li1.val < li2.val:
                tail.next = li1
                li1 = li1.next
            else:
                tail.next = li2
                li2 = li2.next
            tail = tail.next

        if li1:
            tail.next = li1
        if li2:
            tail.next = li2

        return dummy.next

            
# @lc code=end

