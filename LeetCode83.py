# Definition for singly-linked list.
#Given the head of a sorted linked list, delete all duplicates
# such that each element appears only once. Return the linked list sorted as well.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # create an index at head
        cur = head
        # traverse throught the node if the node and the next node exists
        while cur and cur.next:
            # if the value of cur and the value of the next node are the same, we skip
            # the next node
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                #The current node is not the same as the next node in the current node,
                # then cur the node can be kept and continue to access the following nodes
                cur = cur.next
        #  return head would be result
        return head
