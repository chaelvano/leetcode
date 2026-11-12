# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        heap = []

        for i, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, i, head))   # higher sorting priority from left to right (head.val -> i -> head)

        dummy = ListNode()
        curr = dummy

        while heap:
            val, i, node = heapq.heappop(heap)

            curr.next = node
            curr = curr.next
            next = node.next

            if next:
                heapq.heappush(heap, (next.val, i, next))

        return dummy.next
