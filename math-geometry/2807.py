# 2807. Insert Greatest Common Divisors in Linked List


from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        use math.gcd

        def insert_next_node(curr):
            if not curr.next:
                # don't add after last node
                return
            og_next = curr.next
            og_next_val = math.gcd(curr.val, og_next.val)
            insert = ListNode(val=og_next_val, next=og_next)
            curr.next = insert
        '''
        if not head.next:
            return head
        
        def insert_next(curr: ListNode):
            if not curr.next:
                return
            og_next = curr.next
            og_next_val = math.gcd(curr.val, og_next.val)
            insert = ListNode(val=og_next_val, next=og_next)
            curr.next = insert
        
        dummy = head
        while dummy.next:
            insert_next(dummy)
            dummy = dummy.next.next
        return head