# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        while head != None and head.val == val:
            head = head.next
        cur = head
        while cur != None:
            nextptr = cur.next
            if cur.val == val:
                head = cur.next
            if nextptr != None and nextptr.val == val:
                cur.next = nextptr.next
            else:
                cur = cur.next

        return head
        