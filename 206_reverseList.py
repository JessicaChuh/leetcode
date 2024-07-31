#Given the head of a singly linked list, reverse the list, and return the
#reversed list.


head = [1,2,3,4,5]

class Solution:
    def reverseList(self, head):
        head.reverse()
        return head
