# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        # Attach remaining nodes
        current.next = list1 if list1 else list2

        return dummy.next

def build_linked_list(values):
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def print_linked_list(head):
    values = []

    while head:
        values.append(str(head.val))
        head = head.next

    print(" -> ".join(values))


# Mock arguments
list1 = build_linked_list([1, 2, 4])
list2 = build_linked_list([1, 3, 4])

# Run solution
result = Solution().mergeTwoLists(list1, list2)

# Print result
print_linked_list(result)