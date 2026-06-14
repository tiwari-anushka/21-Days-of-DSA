# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        count=0
        while current:
            count+=1
            current=current.next
        middle=count//2
        pointer=head
        for i in range(middle):
            pointer=pointer.next
        return pointer
