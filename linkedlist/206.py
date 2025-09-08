# 206. Reverse Linked List


from typing import Optional
class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        create method to insert at the beginning of list

        def push(node, head) -> head:
            node.next = head
            return node
        
        '''
        if not head:
            return None
                
        res = ListNode(val=head.val)
        ptr = head.next

        while ptr != None:
            new_node = ListNode(val=ptr.val, next=res)
            res=new_node
            ptr=ptr.next
        
        return res