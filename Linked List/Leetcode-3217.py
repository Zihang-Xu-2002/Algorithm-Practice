from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        nums = set(nums) # Very important!
        rtn = dummy
        while dummy and dummy.next:
            while dummy.next and dummy.next.val in nums:
                dummy.next = dummy.next.next
            dummy = dummy.next
        return rtn.next
"""
Set: The average time complexity for checking membership in a set is O(1) 
because sets are implemented as hash tables, allowing for constant-time lookups.

List: Checking membership in a list has a time complexity of O(n), 
where n is the length of the list. This is because lists require a linear search to find the element.
"""