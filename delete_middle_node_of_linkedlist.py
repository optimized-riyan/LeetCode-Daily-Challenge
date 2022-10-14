# Memory inefficient but optimized enough #

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        
        stack = [None, head]
        
        temp = head.next
        while temp != None:
            stack.append(temp)
            temp = temp.next
        
        stack.append(None)
        
        pos = len(stack)//2
        toDel = stack[pos]
        prev = stack[pos - 1]
        
        prev.next = toDel.next
        del(toDel)
        
        return head