# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        arr = []

        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next

        return arr == arr[::-1]
        