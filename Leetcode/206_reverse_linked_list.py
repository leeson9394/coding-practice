# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # if head == None or head.next == None:
        #     return head
        prev = None
           
        while head:
            temp = head  # store current node value to temp
            head = head.next # move head to next node, ready for next cycle
            temp.next = prev # current node pointer point to previous node value
            prev = temp # set prev as current head, ready for next cycle
        return prev


