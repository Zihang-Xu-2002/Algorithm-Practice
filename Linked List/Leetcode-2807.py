from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a: int, b: int) -> int:
            while b != 0:
                a, b = b, a % b
            return a
        start = head
        if head.next is None:
            return head
        else:
            while start and start.next:
                addVal = gcd(start.val, start.next.val)
                addNode = ListNode(addVal)
                tmp = start.next
                start.next = addNode
                addNode.next = tmp
                start = start.next.next
        return head