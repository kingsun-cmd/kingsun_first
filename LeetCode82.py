# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # add one dummy index
        dummy = ListNode(-1)
        dummy.next = head
        # create an index from dummy
        cur = dummy
        # As long as the next node to the currently accessed node exists along
        # with the next node, the access continues
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                value = cur.next.val
                # Using a while loop, keep looking for nodes that have the same value.
                while cur.next and cur.next.val == value:
                    # all the node with same value should skip
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next