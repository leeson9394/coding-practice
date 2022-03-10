# 1 -> 2 -> 3 -> null
# 3 -> 2 -> 1 -> null

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Solution 1, iterative
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None: # base case
            return head
        new_head = None # set reversed linked link head as null
        while head != None: # while all nodes are not visited
            temp = head.next  # store current head pointer, which is node 2 in first round
            head.next = new_head # set current head points to new_head. remove 1->2 and update to 1->null in first round
            new_head = head # move new_head from null to 1 in the first round
            head = temp # move head to node 2 in first round
        return new_head # return node 3

# Step:
# null
# 1 -> null
# 2 -> 1 -> null
# 3 -> 2 -> 1 -> null

# Solution 2, recursive
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None: # base case
            return head
        
        res = self.reverseList(head.next) # recursive next node
        head.next.next = head 
        head.next = None
        return res

# Step:
# 1 -> 2 -> reversed_nodes
# 1 -> 2 <- reversed_nodes
# 1 <- 2 <- reversed_nodes