from typing import Optional, List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # Step 1: Calculate the length of the linked list
        tmp = head
        n = 0
        while tmp:
            n += 1
            tmp = tmp.next
        
        # Step 2: Calculate the size of each part
        x = n // k  # minimum number of nodes in each part
        y = n % k   # number of parts that have one extra node
        
        # Step 3: Split the linked list
        rtn = []
        current = head
        
        for i in range(k):
            part_head = current
            part_size = x + 1 if y > 0 else x  # Determine part size
            y -= 1  # Use up one of the larger parts if needed
            
            # Move current pointer to the end of this part
            prev = None
            for j in range(part_size):
                if current:
                    prev = current
                    current = current.next
            
            # Detach this part from the rest of the list
            if prev:
                prev.next = None
            
            # Append the current part to the result list
            rtn.append(part_head)
        
        # Step 4: Add None parts if fewer than k elements in total
        while len(rtn) < k:
            rtn.append(None)
        
        return rtn
