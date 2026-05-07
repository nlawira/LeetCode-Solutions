# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Instantiate the solution node and required variables.
        solNode = ListNode(0)
        currNode = solNode 
        carry = 0

        # Sum up all the values in l1 and l2 into carry.
        while carry or l1 or l2:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            # Modulus operator because the ones place would be the sum of l1 and l2.
            currNode.next = ListNode(carry%10)
            # The tens place, if it is a 1 because l1 + l2 >= 10, will be carried forward
            # to the next node.
            carry //= 10
            currNode = currNode.next

        # We return the next node of solution node because solution node's current
        # value is 0 when it was instantiated.    
        return solNode.next