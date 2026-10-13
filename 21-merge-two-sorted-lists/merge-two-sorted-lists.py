class Solution(object):
    def mergeTwoLists(self, list1, list2):
        cur1 = list1
        cur2 = list2

        dummy = ListNode(0)
        tail = dummy

        while cur1 != None and cur2 != None:
            if cur1.val <= cur2.val:
                tail.next = ListNode(cur1.val)
                cur1 = cur1.next
            else:
                tail.next = ListNode(cur2.val)
                cur2 = cur2.next

            tail = tail.next

        while cur1 != None:
            tail.next = ListNode(cur1.val)
            cur1 = cur1.next
            tail = tail.next

        while cur2 != None:
            tail.next = ListNode(cur2.val)
            cur2 = cur2.next
            tail = tail.next

        return dummy.next

