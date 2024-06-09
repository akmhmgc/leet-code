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
        heads = []
        for li in lists:
            if not li: continue
            heads.append(li)

        dummy = ListNode(0,None)
        head = dummy

        while len(heads) > 0:
            minHead = min(heads, key=lambda x:x.val)
            head.next = minHead
            head = minHead

            minHeadIndex = heads.index(minHead)
            if minHead.next:
                heads[minHeadIndex] = minHead.next
            else:
                heads.remove(minHead)
        return dummy.next
# @lc code=end

