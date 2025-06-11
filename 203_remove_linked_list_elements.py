from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def toString(self):
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
        return " → ".join(result)

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None: 
            return
        if head.val != val:
            head.next = self.removeElements(head.next, val)
            return head
        return self.removeElements(head.next, val)
    
    @staticmethod
    def createLinkedList(values):
        """Create a linked list from a list of values"""
        if not values:
            return None
        
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
    
solution = Solution()
case = Solution.createLinkedList(values=[1,2,6,3,4,5,6])
print(case.toString())
case = solution.removeElements(case, 6)
print(case.toString())