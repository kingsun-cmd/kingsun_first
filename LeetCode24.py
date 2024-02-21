from typing import List
 class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:


        #Finding recursive termination conditions
             # 1. The node pointed to by head is null.
             # 2. The next node to the node pointed to by head is null.
             # In both cases, a node or a null node is the original head, no matter how the swap operation is performed.

        if head == None or head.next == None:
            return head
        #Keep calling through recursion until it is impossible to recursively continue,
        # the minimum granularity of recursion is at the last node or the last two nodes
        subHead = self.swapPairs(head.next.next)
        headNext = head.next
        # head was pointing to headNext
        # After the swap headNext points to head
        headNext.next = head
        # headNext was pointing to subHead.
        # Now we need head to point to subHead
        head.next = subHead
        return headNext
