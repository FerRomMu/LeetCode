from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.next = next
        self.val = val

#---------------------------------------------------------------------------------------------
# Solution:
#---------------------------------------------------------------------------------------------

def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Adds two non-empty linked lists representing two non-negative integers.

    Each node of the input lists contains a single digit and the digits are stored 
    in reverse order, meaning the 1's digit is at the head of the list. The function 
    returns the sum as a new linked list in the same reversed order.

    Params:
        l1 (Optional[ListNode]): The first linked list representing an integer.
        l2 (Optional[ListNode]): The second linked list representing an integer.

    Returns:
        Optional[ListNode]: A linked list representing the sum of the two integers.
    
    Time Complexity: O(max(n, m)), where n and m are the lengths of l1 and l2.
    Space Complexity: O(max(n, m)) due to the new linked list allocation.
    """
    head = None
    last = None
    carry = 0

    while l1 is not None or l2 is not None or carry:
        value_l1 = l1.val if l1 is not None else 0
        value_l2 = l2.val if l2 is not None else 0
        sum_ls = value_l1 + value_l2 + carry
        
        aux_node = ListNode(val=sum_ls % 10)

        if head is None:
            head = aux_node
            last = head
        else:
            last.next = aux_node
            last = aux_node

        carry = sum_ls // 10
        l1 = l1.next if l1 is not None else l1
        l2 = l2.next if l2 is not None else l2
    
    return head