# Three Pointer Method #

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None:
            return None
        if n == 0:
            return head
        
        # First get size by traversing LL once
        temp = head
        size = 1
        while temp != None:
            temp = temp.next
            size += 1
        
        # Use 3 pointers,
        # t: points node to be deleted
        # t1: points node previous to t
        # t2: pointer to node after t
        t1, t, t2 = None, head, head.next
        # loop to move the 3 ptrs
        for _ in range(size - n - 1):
            t1 = t
            t = t2
            t2 = t2.next
        
        if t1 != None:
            t1.next = t2
        else:
            # If t1 is null, the node to be deleted is the head,
            # new head will be t2
            head = t2
        del(t)
        
        return head