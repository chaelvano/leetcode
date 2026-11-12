# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(next=head)
        prev = dummy

        while prev.next and prev.next.next:
            curr = prev.next
            next = curr.next

            curr.next = next.next
            next.next = curr
            prev.next = next

            prev = curr

        return dummy.next
